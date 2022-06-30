r_json_filename = "res"
r_csv_filename = "res"
r_coef_filename = "res_coef"
r_info_filename = "res_info"
mean_filename = "mean"

dir_json = "res_json"
max_coef = 3
categories = ("good", "normal", "bad", "very bad")
columns_to_coef = {  # name_column : coef || where 0 - None -5 - bad/ 5 - good
    'iso_code': 0,
    'continent': 0,
    'location': 0,
    'date': 0,

    # 'total_cases': -3.5, # -
    # 'new_cases' : -4.5, # -
    # 'new_cases_smoothed' : -4.5, # -
    # 'total_deaths' : -3.5,
    # 'new_deaths' : -4.5,
    # 'new_deaths_smoothed' : -4.5,
    'total_cases_per_million': -4,
    # 'new_cases_per_million' : ,
    'new_cases_smoothed_per_million': -5,
    'total_deaths_per_million': -1,
    # 'new_deaths_per_million' : ,
    'new_deaths_smoothed_per_million': -1,

    'reproduction_rate': -5,

    # 'icu_patients' : ,
    # 'icu_patients_per_million' : -2, # 13 процентов
    # 'hosp_patients' : ,
    # 'hosp_patients_per_million' : -2.5, # 13 процентов
    # 'weekly_icu_admissions' : ,
    # 'weekly_icu_admissions_per_million' : -3, # составляет 3 процентов
    # 'weekly_hosp_admissions' : ,
    # 'weekly_hosp_admissions_per_million' : -3, # составляет 6 процентов
    # 'total_tests' : ,
    # 'new_tests' : ,
    'total_tests_per_thousand': 1.5,
    # 'new_tests_per_thousand' : 4,
    # 'new_tests_smoothed' : ,
    'new_tests_smoothed_per_thousand': 3,
    'positive_rate': -2,
    # 'tests_per_case' :  , # HZ
    # 'tests_units' : , # HZ
    # 'total_vaccinations' : 3.5,
    # 'people_vaccinated' : 4.3,
    # 'people_fully_vaccinated' : 3,
    # 'total_boosters' : 2.5,
    # 'new_vaccinations' : 4,
    # 'new_vaccinations_smoothed' : 4,
    'total_vaccinations_per_hundred': 2,
    'people_vaccinated_per_hundred': 5,
    'people_fully_vaccinated_per_hundred': 3.5,
    # 'total_boosters_per_hundred' : 3, # очень мало. менее 13 процентов
    'new_vaccinations_smoothed_per_million': 3.5,
    # 'new_people_vaccinated_smoothed' : ,
    'new_people_vaccinated_smoothed_per_hundred': 4.5,

    'stringency_index': 8,
    'population': 0,
    'population_density': 3,
    'median_age': -5,
    'aged_65_older': -2,
    'aged_70_older': -1,
    'gdp_per_capita': 3,
    'extreme_poverty': -4,
    # 'cardiovasc_death_rate' : , # хз. Тип из-за слабого иммунитета они могут заболеть чаще? Или Умирают хотя могли умереть от сердца
    # 'diabetes_prevalence' : ,
    'female_smokers': -2.5,
    'male_smokers': -2,
    'handwashing_facilities': 4,
    'hospital_beds_per_thousand': 3,
    # 'life_expectancy' : , # HZ
    'human_development_index': 5,
    # 'excess_mortality_cumulative_absolute' : ,
    # 'excess_mortality_cumulative' : ,
    # 'excess_mortality' : ,
    # 'excess_mortality_cumulative_per_million' :
}
