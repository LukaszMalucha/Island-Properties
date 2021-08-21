# -*- coding: utf-8 -*-
"""
Created on Thu May  6 19:16:43 2021

@author: LukaszMalucha
"""
import pandas as pd
import numpy as np


dataset = pd.read_csv("PPR-ALL.csv", encoding="iso-8859-1")


dataset = dataset.rename(columns = {"Date of Sale (dd/mm/yyyy)": "date", 
                                    "Address": "address", 
                                    "County": "county", 
                                    "Price ()": "price", 
                                    "Description of Property": "description",
                                    "Property Size Description": "size"})



dataset = dataset[["date", "address", "county", "price", "description", "size"]]



dataset["price"] = dataset["price"].str.replace("", "").str.replace(",", "")
dataset["price"] = dataset["price"].str.split(".").str[0]




dataset["size"] = dataset["size"].str.replace("níos mó ná nó cothrom le 38 méadar cearnach agus níos lú ná 125 méadar cearnach", "greater than or equal to 38 sq metres and less than 125 sq metres")
dataset["size"] = np.where(dataset["size"].str.contains("cearnach"), "less than 38 sq metres", dataset["size"])
dataset["size"] = dataset["size"].fillna("None")


dataset["size"] = dataset["size"].str.replace("less than 38 sq metres", "1-38 m2")
dataset["size"] = dataset["size"].str.replace("greater than or equal to 38 sq metres and less than 125 sq metres", "38-125 m2")
dataset["size"] = dataset["size"].str.replace("greater than 125 sq metres", "125-1000 m2")
dataset["size"] = dataset["size"].str.replace("greater than or equal to 125 sq metres", "125-1000 m2")

sizes = list(dataset["size"].unique())

dataset["date"] = dataset["date"].str.split("/")
dataset["date"] = dataset["date"].str[2] + "-" + dataset["date"].str[1] + "-" + dataset["date"].str[0]

dataset["description"] = dataset["description"].str.replace("Teach/Árasán Cónaithe Atháimhe", "Second-Hand Dwelling house /Apartment")
dataset["description"] = dataset["description"].str.replace("Teach/Árasán Cónaithe Nua", "New Dwelling house /Apartment")
dataset["description"] = np.where(dataset["description"].str.contains("Nua"), "New Dwelling house /Apartment", dataset["description"])
dataset["description"] = dataset["description"].str.replace("Second-Hand Dwelling house /Apartment", "second-hand")
dataset["description"] = dataset["description"].str.replace("New Dwelling house /Apartment", "new")

description = list(dataset["description"].unique())

n3 = dataset[dataset["address"].str.contains("Millers Court")]
heathfield = dataset[dataset["address"].str.contains("heathfield")]


dataset.to_csv("sold_properties.csv", index=False)










