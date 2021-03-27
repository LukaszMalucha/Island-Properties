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
###################################### https://www.ecdc.europa.eu/en/publications-data/data-national-14-day-notification-rate-covid-19

import pandas as pd
import datetime


dataset_weekly = pd.read_csv("covid_weekly_org.csv", encoding="utf-8")

col = list(dataset_weekly.columns)

dataset_weekly = dataset_weekly[dataset_weekly["continent"] == "Europe"]

dataset_weekly_cases = dataset_weekly[dataset_weekly["indicator"] == "cases"]
dataset_weekly_cases = dataset_weekly_cases[["country", "weekly_count", "year_week"]]
dataset_weekly_cases = dataset_weekly_cases.rename(columns={"weekly_count":"cases"})



dataset_weekly_deaths = dataset_weekly[dataset_weekly["indicator"] == "deaths"]
dataset_weekly_deaths = dataset_weekly_deaths[["country", "weekly_count", "year_week"]]

dataset_weekly_deaths = dataset_weekly_deaths.rename(columns={"weekly_count":"deaths"})

dataset_weekly = dataset_weekly_cases.merge(dataset_weekly_deaths, on=["country","year_week"])



dataset_weekly["country"] = dataset_weekly["country"].str.replace("_", " ")


dataset_weekly["date"] = dataset_weekly["year_week"].apply(lambda x: datetime.datetime.strptime(x + '-1', "%Y-%W-%w"))
dataset_weekly["date"] = dataset_weekly["date"].astype(str)        


## REMOVE THAT EXTRA WEEK IN BETWEEN 
dataset_weekly = dataset_weekly[dataset_weekly["year_week"] != "2020-53"  ]




dataset_weekly = dataset_weekly.drop("year_week", axis=1)


    

dataset_weekly.to_csv("covid_weekly.csv", index = False)


###################################### Testing Rates Both Datasets (positivty & testing 1st and 3rd map)  https://ourworldindata.org/coronavirus-testing   


dataset_testing = pd.read_csv("daily-tests-per-thousand-people-smoothed-7-day.csv", encoding="utf-8")
dataset_testing = dataset_testing[["Entity", "Day","new_tests_per_thousand_7day_smoothed"]]
dataset_testing = dataset_testing.rename(columns={"Entity": "country", "new_tests_per_thousand_7day_smoothed": "testing_rate", "Day": "date"})
dataset_testing = dataset_testing.sort_values(by=["date"], ascending=False)
dataset_testing["d"] = dataset_testing["country"].duplicated(keep="first")
dataset_testing = dataset_testing[dataset_testing["d"] == False]





dataset_positivity = pd.read_csv("positive-rate-daily-smoothed.csv", encoding="utf-8")
dataset_positivity = dataset_positivity[["Entity", "Day","short_term_positivity_rate"]]
dataset_positivity = dataset_positivity.rename(columns={"Entity": "country", "short_term_positivity_rate": "positivity_rate", "Day": "date"})
dataset_positivity = dataset_positivity.sort_values(by=["date"], ascending=False)
dataset_positivity["d"] = dataset_positivity["country"].duplicated(keep="first")
dataset_positivity = dataset_positivity[dataset_positivity["d"] == False]


dataset_testing = dataset_testing.merge(dataset_positivity, on=["country"])

dataset_testing = dataset_testing[["country", "testing_rate","positivity_rate" ]]


#dataset_testing = pd.read_csv("covid_testing_org.csv", encoding="utf-8")
#
#col = list(dataset_testing.columns)
#
#
#dataset_testing["d"] = dataset_testing["country"].duplicated(keep="last")
#dataset_testing_weeks = dataset_testing[dataset_testing["d"] == False]
#
#dataset_testing_weeks = dataset_testing_weeks[["country", "testing_rate", "positivity_rate" ]]

dataset_testing.to_csv("covid_testing.csv", index = False)



####################################

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def country_checker(string):
        if string in countries:
            return True
        
      

dataset_1 = pd.read_csv("covid_weekly.csv", encoding="utf-8")
dataset_2 = pd.read_csv("country_medical.csv", encoding="utf-8")
dataset_3 = pd.read_csv("covid_testing.csv", encoding="utf-8")
dataset_4 = pd.read_csv("population.csv", encoding="utf-8")

dataset_1["country"] = dataset_1["country"].str.replace("Czechia", "Czech Republic")
dataset_3["country"] = dataset_3["country"].str.replace("Czechia", "Czech Republic")
dataset_4["country"] = dataset_4["country"].str.replace("Slovak Republic", "Slovakia")

countries = list(dataset_2["country"].unique())  
countries_3 = list(dataset_3["country"].unique())  

dataset_final = dataset_1.merge(dataset_2, how="left", on=["country"]) 

dataset_final["check"]  = dataset_final["country"].apply(lambda x: country_checker(x))    
dataset_final = dataset_final[dataset_final["check"] == True]
dataset_final = dataset_final.drop("check", axis =1 )





dataset_final = dataset_final.merge(dataset_3, how="left", on=["country"]) 
dataset_final = dataset_final[~dataset_final["testing_rate"].isnull()]



dataset_final = dataset_final.merge(dataset_4, how="left", on=["country"]) 


dataset_final = dataset_final.drop_duplicates()








dataset_final["check"] = dataset_final["country"].apply(lambda x: country_checker(x))

dataset_final = dataset_final[dataset_final["check"] == True]

dataset_final["cases"] = dataset_final["cases"].abs()
dataset_final["deaths"] = dataset_final["deaths"].abs()
dataset_final["cases"] = dataset_final["cases"]

dataset_final = dataset_final.drop("check", axis =1 )
dataset_final["cases_per_capita"] = dataset_final["cases"] / dataset_final["Population"] 


lst = list(dataset_final.columns)

scaler = MinMaxScaler()


dataset_final["deaths_per_capita"] = round((dataset_final["deaths"] / dataset_final["Population"]), 6)

dataset_final[["cases_per_capita", 'median_age', 'gdp_per_capita', 'diabetes_prevalence', 'curative_beds_per_hundred_thousand', 'life_expectancy', 'testing_rate', 'positivity_rate', ]] = scaler.fit_transform(dataset_final[["cases_per_capita", 'median_age', 'gdp_per_capita', 'diabetes_prevalence', 'curative_beds_per_hundred_thousand', 'life_expectancy', 'testing_rate', 'positivity_rate']].values)



dataset_final["severity_ratio"] = (dataset_final["cases_per_capita"]  + (dataset_final['positivity_rate'] * 0.8 ) + (dataset_final['median_age'] * 0.4 ))  / (dataset_final['curative_beds_per_hundred_thousand'] * 1.8  + dataset_final['testing_rate'] * 1.8 + dataset_final['life_expectancy'] * 1.4 + dataset_final['gdp_per_capita'] * 1.4) * 10





dataset_final.to_csv("dataset_covid.csv", index=False)












