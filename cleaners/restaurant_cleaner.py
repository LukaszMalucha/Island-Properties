# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:47:52 2020

@author: LukaszMalucha
"""

import pandas as pd
import numpy as np

dataset=pd.read_csv("restaurants.csv",  encoding="utf-8") 

dataset=dataset.drop_duplicates()
dataset=dataset[dataset["title"] != "title"]



dataset["locality"]=np.where(dataset["locality"].str.contains("386"),"Adeje",dataset["locality"])
dataset["locality"]=np.where(dataset["locality"].str.contains("Tenerife"),"Adeje",dataset["locality"])
dataset["locality"]=np.where(dataset["locality"].str.contains("Av. V Centenario 1"),"Adeje",dataset["locality"])
dataset["locality"]=np.where(dataset["locality"].str.contains("Fanabe"),"Adeje",dataset["locality"])
dataset["locality"]=np.where(dataset["locality"].str.contains("Pueblo Canario 112 Playa de las Americas"),"Playa de Las Americas",dataset["locality"])

unique_locality= list(dataset["locality"].unique())

dataset["cuisine_1"]=dataset["cuisine"].str.split(", ").str[0]
dataset["cuisine_2"]=dataset["cuisine"].str.split(", ").str[1]
dataset["cuisine_3"]=dataset["cuisine"].str.split(", ").str[2]


dataset=dataset[["title","address","rating","cuisine_1","cuisine_2","cuisine_3", "link"]]


dataset=dataset.fillna("")


dataset.to_csv("restaurants_cleaned.csv",index=False) 


