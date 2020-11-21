# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:57:34 2020

@author: LukaszMalucha
"""


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
###################################### https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide

import pandas as pd


dataset_daily = pd.read_csv("covid_daily_org.csv", encoding="utf-8")

col = list(dataset_daily.columns)

dataset_daily = dataset_daily[["dateRep", "cases", "deaths", "countriesAndTerritories"]]

dataset_daily = dataset_daily.rename(columns= {"countriesAndTerritories": "country"})


dataset_daily["country"] = dataset_daily["country"].str.replace("_", " ")

dataset_daily.to_csv("covid_daily.csv", index = False)

#
#
###################################### https://www.ecdc.europa.eu/en/publications-data/covid-19-testing



dataset_testing = pd.read_csv("covid_testing_org.csv", encoding="utf-8")

col = list(dataset_testing.columns)


dataset_testing["d"] = dataset_testing["country"].duplicated(keep="last")
dataset_testing_weeks = dataset_testing[dataset_testing["d"] == False]

dataset_testing_weeks = dataset_testing_weeks[["country", "testing_rate", "positivity_rate" ]]

dataset_testing_weeks.to_csv("covid_testing.csv", index = False)



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












