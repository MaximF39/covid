import json
import os

import numpy as np
import pandas as pd
import requests

from config import max_coef, categories, columns_to_coef, dir_json, r_json_filename, r_csv_filename, r_coef_filename, \
    r_info_filename, mean_filename

all_name_columns = (k for k in columns_to_coef.keys())


class T_CreateFile:
    json = ".json"
    csv = ".csv"


def create_file(obj, filename, type_):
    if filename:
        full_filename = filename + type_
        full_path = os.path.join(dir_json, full_filename)
        if type_ == T_CreateFile.json:
            with open(full_path, 'w') as f:
                json.dump(obj, f, indent=4)
        elif type_ == T_CreateFile.csv:
            def dict_to_dataframe(obj):
                df = pd.DataFrame(columns=['country', "res"])
                for i in range(len(categories)):
                    for k, v in obj[categories[i]].items():
                        df = df.append({'country': k, "res": v["res"]}, ignore_index=True)
                return df

            df = dict_to_dataframe(obj)
            with open(full_path, 'w') as f:
                df.to_csv(f)


def parse():
    df = pd.DataFrame(pd.read_csv("owid-covid-data.csv"))
    df['date'] = ((pd.to_datetime(df['date']) - pd.to_datetime('2021-01-01')) / np.timedelta64(1, 'D')).astype(int)
    df = df.drop(df[df['date'] < 0].index)
    df = df[[*all_name_columns]]
    return df


def finds_mean(df, mean_filename):
    d = {}
    for c in columns_to_coef:
        if columns_to_coef[c] == 0:
            continue
        mean_ = df.groupby(['iso_code']).mean().describe().loc["mean"][c]  # mean
        d[f"{c}_mean"] = mean_
    globals().update(d)
    create_file(d, mean_filename, T_CreateFile.json)


def get_result(df):
    res_df = {}
    df_mean = df.groupby("iso_code").mean()
    for index, country in enumerate(
            pd.DataFrame(df.apply(pd.unique)).rename(columns={0: 'Unique values'}).iloc[0]["Unique values"]):
        df_ = df_mean.loc[country]
        res_df[country] = {}
        res = 0
        for c in columns_to_coef.keys():
            if columns_to_coef[c] == 0 or pd.isna(df_[c]):
                continue
            raz = df_[c] / eval(f"{c}_mean")  # 0 - 1
            if raz > max_coef:
                raz = max_coef
            res_df[country][c] = columns_to_coef[c] * raz
            res += columns_to_coef[c] * raz
        res_df[country]['res'] = res
    return res_df


def sort_result(res_dict):
    res_dict = dict(sorted(res_dict.items(), key=lambda item: item[1]["res"], reverse=True))
    gr = len(res_dict) // len(categories)
    d_ = {}
    for i in range(len(categories)):
        if i != len(categories) - 1:
            d_[categories[i]] = {k: res_dict[k] for k in list(res_dict)[gr * i: gr * (i + 1)]}
        else:
            d_[categories[i]] = {k: res_dict[k] for k in list(res_dict)[gr * i:]}
    return d_


def save_file(res_dict,
              r_json_filename, r_csv_filename,
              r_coef_filename, r_info_filename):
    if r_json_filename:
        new_d = {}
        for i in range(len(categories)):
            new_d[categories[i]] = {}
            for k, v in res_dict[categories[i]].items():
                new_d[categories[i]][k] = v['res']
        create_file(new_d, r_json_filename, T_CreateFile.json)

    create_file(res_dict, r_csv_filename, T_CreateFile.csv)
    create_file(columns_to_coef, r_coef_filename, T_CreateFile.json)
    create_file(res_dict, r_info_filename, T_CreateFile.json)


def main():
    df = parse()
    finds_mean(df, mean_filename)
    res_dict = get_result(df)
    res_dict = sort_result(res_dict)
    save_file(
        res_dict,
        r_json_filename, r_csv_filename,
        r_coef_filename, r_info_filename,
    )


def change_cat(cat):
    index = tuple(i for i in range(len(cat)))
    return dict(zip(index, cat))


if __name__ == '__main__':
    list_dir = os.listdir()
    if dir_json not in list_dir:
        os.mkdir(dir_json)
    file_csv = "owid-covid-data.csv"
    if file_csv not in list_dir:
        print("Скачивание файла")
        response = requests.get("https://covid.ourworldindata.org/data/owid-covid-data.csv")
        open(file_csv, "wb").write(response.content)
    categories = change_cat(categories)
    print("Начало обучения")
    main()
