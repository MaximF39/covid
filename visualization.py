import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from main import columns_to_coef

def show_corr():
    df = pd.read_csv("owid-covid-data.csv")
    all_name_columns = (k for k in columns_to_coef.keys())
    df = df[[*all_name_columns]]
    heatmap = sns.heatmap(df.corr(), vmin=-1, vmax=1, annot=False)
    heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':8}, pad=8)
    plt.show()
