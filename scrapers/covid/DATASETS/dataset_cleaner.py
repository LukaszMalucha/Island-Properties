# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:57:34 2020

@author: LukaszMalucha
"""

#import pandas as pd
#
#dataset = pd.read_csv("country_medical.csv", encoding="utf-8")
#
#
#dataset = dataset[["location", "median_age", "gdp_per_capita", "diabetes_prevalence", "handwashing_facilities", "hospital_beds_per_thousand", "life_expectancy"]]
#
#dataset = dataset.rename(columns= {"location": "country"})
#
#dataset = dataset.drop_duplicates()
#
#
#dataset.to_csv("country_medical.csv", index = False)
#
######################################
#
#
#
#
#dataset = pd.read_csv("covid_daily.csv", encoding="utf-8")
#
#col = list(dataset.columns)
#
#dataset = dataset[["dateRep", "cases", "deaths", "countriesAndTerritories"]]
#
#dataset = dataset.rename(columns= {"countriesAndTerritories": "country"})
#
#
#dataset["country"] = dataset["country"].str.replace("_", " ")
#
#dataset.to_csv("covid_daily.csv", index = False)
#
#
#
######################################
#
#
#
#
#dataset = pd.read_csv("covid_testing.csv", encoding="utf-8")
#
#col = list(dataset.columns)
#
#
#dataset["d"] = dataset["country"].duplicated(keep="last")
#dataset_weeks = dataset[dataset["d"] == False]
#
#dataset_weeks = dataset_weeks[["country", "testing_rate", "positivity_rate" ]]
#
#dataset_weeks.to_csv("covid_testing.csv", index = False)
#
####################################

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def country_checker(string):
        if string in countries:
            return True

dataset_1 = pd.read_csv("covid_daily.csv", encoding="utf-8")
dataset_2 = pd.read_csv("country_medical.csv", encoding="utf-8")
dataset_3 = pd.read_csv("covid_testing.csv", encoding="utf-8")
dataset_4 = pd.read_csv("population.csv", encoding="utf-8")

dataset_1["country"] = dataset_1["country"].str.replace("Czechia", "Czech Republic")
dataset_3["country"] = dataset_3["country"].str.replace("Czechia", "Czech Republic")
dataset_4["country"] = dataset_4["country"].str.replace("Slovak Republic", "Slovakia")

#dataset_2["check"]  = dataset_2["country"].apply(lambda x: country_checker(x))    
#dataset_2 = dataset_2[dataset_2["check"] == True]
#dataset_2 = dataset_2.drop("check", axis =1 )
#dataset_2.to_csv("country_medical.csv", index=False)

dataset_final = dataset_1.merge(dataset_2, how="left", on=["country"]) 

dataset_final = dataset_final.merge(dataset_3, how="left", on=["country"]) 

dataset_final = dataset_final.merge(dataset_4, how="left", on=["country"]) 


dataset_final = dataset_final.drop_duplicates()

countries = list(dataset_3["country"].unique())



        
    



dataset_final["check"] = dataset_final["country"].apply(lambda x: country_checker(x))

dataset_final = dataset_final[dataset_final["check"] == True]

dataset_final["cases"] = dataset_final["cases"].abs()
dataset_final["deaths"] = dataset_final["deaths"].abs()
dataset_final["cases"] = dataset_final["cases"]

dataset_final = dataset_final.drop("check", axis =1 )
dataset_final["cases_per_capita"] = dataset_final["cases"] / dataset_final["Population"] 


lst = list(dataset_final.columns)

scaler = MinMaxScaler()

dataset_final[["cases_per_capita", 'median_age', 'gdp_per_capita', 'diabetes_prevalence', 'curative_beds_per_hundred_thousand', 'life_expectancy', 'testing_rate', 'positivity_rate', ]] = scaler.fit_transform(dataset_final[["cases_per_capita", 'median_age', 'gdp_per_capita', 'diabetes_prevalence', 'curative_beds_per_hundred_thousand', 'life_expectancy', 'testing_rate', 'positivity_rate']].values)









dataset_final.to_csv("dataset_covid.csv", index=False)


















