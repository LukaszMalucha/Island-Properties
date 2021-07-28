# -*- coding: utf-8 -*-
"""
Created on Thu May  6 19:16:43 2021

@author: LukaszMalucha
"""

import pandas as pd
import numpy as np






"""
CONCAT OFFERS
"""




dataset_1 = pd.read_csv("ballincollig_offers_2021.csv", encoding="utf-8")
dataset_2 = pd.read_csv("ballincollig_offers_2019.csv", encoding="utf-8")
dataset_3 = pd.read_csv("ballincollig_mitula.csv", encoding="utf-8")


dataset_2 = dataset_2[dataset_2["price"] != 'rice On Application']

dataset_1["date"] = dataset_1["date"].str.replace("Jul-26-2021", "2021-07-26")

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


dataset = pd.concat([dataset_1, dataset_2, dataset_3])


dataset = dataset.sort_values("date", ascending=False)


dataset["duplicate"] = dataset.duplicated(subset=['address', 'price'])
dataset = dataset[dataset["duplicate"] == False]
dataset = dataset.drop(["duplicate", "geocode"], axis=1)


dataset["lat"] = np.where(dataset["area"] == "Old Quarter", "51.89120011526423", dataset["lat"])
dataset["long"] = np.where(dataset["area"] == "Old Quarter", "-8.597460712163135", dataset["long"])


dataset.to_csv("ballincollig_full_offers.csv", index=False)










