# -*- coding: utf-8 -*-
"""
Created on Thu May  6 19:16:43 2021

@author: LukaszMalucha
"""

import pandas as pd
import numpy as np






"""
POPULARITY
"""




dataset = pd.read_csv("ballincollig_offers_2021.csv", encoding="utf-8")
dataset["date"] = dataset["date"].str.replace("Jul-26-2021", "2021-07-26")

dataset = dataset[["address", "date","popularity"]]



dataset_dates = dataset.pivot(index="address", columns="date", values="popularity")

dataset_dates = dataset_dates.fillna(0)


dataset_dates.to_csv("ballincollig_popularity.csv")









