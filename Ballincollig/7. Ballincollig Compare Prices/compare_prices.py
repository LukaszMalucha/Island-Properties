# -*- coding: utf-8 -*-
"""
Created on Thu May  6 19:16:43 2021

@author: LukaszMalucha
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
todays_date = today.strftime("%Y-%m-%d")
yesterday_date = yesterday.strftime("%Y-%m-%d")


CURRENT_DATASETS_PATH = Path(Path.cwd().parent, "_DATASETS")


"""
CONCAT OFFERS
"""



dataset_2 = pd.read_csv("ballincollig_offers_2019.csv", encoding="utf-8")
dataset_3 = pd.read_csv("ballincollig_mitula.csv", encoding="utf-8")


dataset_2 = dataset_2[dataset_2["price"] != 'rice On Application']


dataset_2["date"] = "2019-06-12"
dataset_2["link"] = "None"
dataset_2["popularity"] = 0
dataset_2["size"] = 0
dataset_2["price"] = dataset_2["price"].astype(int)


dataset_3["date"] = "2019-06-12"
dataset_3["link"] = "Mitula"
dataset_3["popularity"] = 0
dataset_3["size"] = 0
dataset_3["price"] = dataset_3["price"].astype(int)
dataset_3["property_type"] = "None"


dataset = pd.concat([dataset_2, dataset_3])


dataset = dataset.sort_values("date", ascending=False)

dataset["address"] = dataset["address"].str.replace(",", " ")
dataset["address"] = dataset["address"].str.replace("Benamara ", "")
dataset["address"] = dataset["address"].str.replace("Apartment", "")
dataset["address"] = dataset["address"].str.replace("Oldcourt", "Old Court")
dataset["address"] = dataset["address"].str.strip()

dataset["number"] = dataset["address"].str.split(" ").str[0]

dataset["lat"] = np.where(dataset["area"] == "Old Quarter", "51.89120011526423", dataset["lat"])
dataset["long"] = np.where(dataset["area"] == "Old Quarter", "-8.597460712163135", dataset["long"])








dataset["matcher"] = dataset["address"].str.replace("1", "")
dataset["matcher"] = dataset["matcher"].str.replace("57a", "")
dataset["matcher"] = dataset["matcher"].str.replace("57A", "")
dataset["matcher"] = dataset["matcher"].str.replace("2", "")
dataset["matcher"] = dataset["matcher"].str.replace("3", "")
dataset["matcher"] = dataset["matcher"].str.replace("4", "")
dataset["matcher"] = dataset["matcher"].str.replace("5", "")
dataset["matcher"] = dataset["matcher"].str.replace("6", "")
dataset["matcher"] = dataset["matcher"].str.replace("7", "")
dataset["matcher"] = dataset["matcher"].str.replace("8", "")
dataset["matcher"] = dataset["matcher"].str.replace("9", "")
dataset["matcher"] = dataset["matcher"].str.replace("The", "")
dataset["matcher"] = dataset["matcher"].str.replace("The", "")
dataset["matcher"] = dataset["matcher"].str.replace("An", "")
dataset["matcher"] = dataset["matcher"].str.replace("  ", " ")
dataset["matcher"] = dataset["matcher"].str.replace(",", "")
dataset["matcher"] = dataset["matcher"].str.replace("Caisleé", "Caisleán")
dataset["matcher"] = dataset["matcher"].str.replace("Caislean", "Caisleán")
dataset["matcher"] = dataset["matcher"].str.split(" ").str[1]


dataset = dataset.sort_values("price", ascending=False)
dataset["duplicate"] = dataset.duplicated(subset=['matcher', 'number', 'area'])





dataset = dataset[dataset["matcher"].notnull()]
dataset = dataset[dataset["duplicate"] == False]
dataset = dataset[dataset["address"] != "72 Old Court  Greenfields  Killumney Road  Ballincollig  Co. Cork"]
dataset = dataset.drop(["duplicate", "geocode", "date"], axis=1)







"""
PRICE COMPARISON
"""


dataset_sold = pd.read_csv("ballincollig_sold.csv", encoding="utf-8")

dataset_sold = dataset_sold[['area', 'address', 'full_address', 'number', 'price', 'date']]






dataset_sold["matcher"] = dataset_sold["full_address"].str.replace("1", "")
dataset_sold["matcher"] = dataset_sold["matcher"].str.replace("57a", "")
dataset_sold["matcher"] = dataset_sold["matcher"].str.replace("A ", "")
dataset_sold["matcher"] = dataset_sold["matcher"].str.replace("2", "")
dataset_sold["matcher"] = dataset_sold["matcher"].str.replace("3", "")
dataset_sold["matcher"] = dataset_sold["matcher"].str.replace("4", "")
dataset_sold["matcher"] = dataset_sold["matcher"].str.replace("5", "")
dataset_sold["matcher"] = dataset_sold["matcher"].str.replace("6", "")
dataset_sold["matcher"] = dataset_sold["matcher"].str.replace("7", "")
dataset_sold["matcher"] = dataset_sold["matcher"].str.replace("8", "")
dataset_sold["matcher"] = dataset_sold["matcher"].str.replace("9", "")
dataset_sold["matcher"] = dataset_sold["matcher"].str.replace("The", "")
dataset_sold["matcher"] = dataset_sold["matcher"].str.replace("The", "")
dataset_sold["matcher"] = dataset_sold["matcher"].str.replace("An", "")
dataset_sold["matcher"] = dataset_sold["matcher"].str.replace("  ", " ")
dataset_sold["matcher"] = dataset_sold["matcher"].str.replace(",", "")
dataset_sold["matcher"] = dataset_sold["matcher"].str.replace("Caislean", "Caisleán")




dataset_sold["matcher"] = dataset_sold["matcher"].str.split(" ").str[1]


dataset_sold = dataset_sold.rename(columns={"price": "price_sold"})
dataset_sold = dataset_sold.rename(columns={"address": "address_sold"})

dataset_sold = dataset_sold[dataset_sold["number"].notnull()]



dataset_matcher = dataset.merge(dataset_sold, on=["area", "number", "matcher"], how="left")



dataset_no_match = dataset_matcher[dataset_matcher["price_sold"].isnull()]


dataset_no_match = dataset_no_match[["address","area", "number", "matcher"]]

dataset_sold_match = dataset_sold[["matcher","number","area","full_address"]]





dataset_matcher = dataset_matcher[dataset_matcher["price_sold"].notnull()]





dataset_matcher["price_difference"] = (dataset_matcher["price_sold"] - dataset_matcher["price"]) / dataset_matcher["price"]




dataset_matcher["year"] = dataset_matcher["date"].str.split("-").str[0]

dataset_avg_price_difference = dataset_matcher.groupby(["year"])["price_difference"].mean()
dataset_avg_price_difference = dataset_avg_price_difference.reset_index()
dataset_avg_price_difference = dataset_avg_price_difference.rename(columns={"price_difference": "annual_avg_price_difference"})




dataset_matcher = dataset_matcher.merge(dataset_avg_price_difference, on="year", how="left")
dataset_matcher = dataset_matcher.drop("year", axis=1)
#dataset_matcher = dataset_matcher.rename(columns={""})

dataset_matcher.to_csv(Path(CURRENT_DATASETS_PATH, f"{todays_date}_ballincollig_compare_prices.csv"))















