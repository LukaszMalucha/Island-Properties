# -*- coding: utf-8 -*-
"""
Created on Thu May  6 19:16:43 2021

@author: LukaszMalucha
"""

import pandas as pd
import numpy as np






"""
PRICE COMPARISON
"""


dataset_sold = pd.read_csv("ballincollig_sold.csv", encoding="utf-8")

dataset_sold = dataset_sold[['area', 'address', 'full_address', 'number', 'price',]]


dataset_1 = pd.read_csv("ballincollig_offers_2021.csv", encoding="utf-8")
dataset_2 = pd.read_csv("ballincollig_offers_2019.csv", encoding="utf-8")
dataset_3 = pd.read_csv("ballincollig_mitula.csv", encoding="utf-8")


dataset_1 = dataset_1[['area', 'address', 'price']]
dataset_2 = dataset_2[['area','address', 'price',]]
dataset_3 = dataset_3[['area','address', 'price',]]



dataset = pd.concat([dataset_1, dataset_2, dataset_3])

dataset = dataset[dataset["price"] != "rice On Application"]

dataset["price"] = dataset["price"].astype(int)



dataset["number"] = dataset["address"].str.split(" ").str[0]

dataset["matcher"] = dataset["address"].str.replace("1", "")
dataset["matcher"] = dataset["matcher"].str.replace("57a", "")
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

dataset["matcher"] = dataset["matcher"].str.split(" ").str[1]






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

dataset_sold["matcher"] = dataset_sold["matcher"].str.split(" ").str[1]


dataset_sold = dataset_sold.rename(columns={"price": "price_sold"})
dataset_sold = dataset_sold.rename(columns={"address": "address_sold"})


dataset_matcher = dataset.merge(dataset_sold, on=["area", "number", "matcher"], how="left")

dataset_matcher = dataset_matcher[dataset_matcher["price_sold"].notnull()]


dataset_matcher.to_csv("ballincollig_compare.csv", index=False)






















