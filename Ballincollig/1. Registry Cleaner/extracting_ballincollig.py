# -*- coding: utf-8 -*-
"""
Created on Thu May  6 19:16:43 2021

@author: LukaszMalucha
"""
import pandas as pd
import numpy as np


#dataset = pd.read_csv("sold_properties.csv", encoding="iso-8859-1")
#dataset = dataset[dataset["county"] == "Cork"]
#dataset.to_csv("cork_sold.csv", index=False)



dataset = pd.read_csv("cork_sold.csv", encoding="utf-8")


dataset["address"] = dataset["address"].str.title()
dataset["locality_string"] = dataset["address"].str.split(", ").str[-1]




dataset["locality"] = ""
dataset["locality"] = np.where(dataset["locality_string"].str.contains(" "), "Cork", dataset["locality"])

dataset["locality"] = np.where(dataset["address"].str.contains("\..."), "Cork", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Street"), "Cork", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Road"), "Cork", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Carrigaline"), "Carrigaline", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Glounthaune"), "Glounthaune", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Ballincol"), "Ballincollig", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Ballingcol"), "Ballincollig", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Ballinco"), "Ballincollig", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Ballincough"), "Ballincough", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Ballycotto"), "Ballycotton", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Ballyphenhane"), "Ballyphehane", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Beaumont"), "Beaumount", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Blafrney"), "Blarney", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Buttervant"), "Buttevant", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Buttervent"), "Buttevant", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Carig"), "Carrigaline", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Cariig"), "Carrigaline", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Carrag"), "Carrigaline", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Carriaga"), "Carrigaline", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Ballinhassiq"), "Ballinhassig", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Ballinspitle"), "Ballinspittle", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Ballyvoloon"), "Ballyvolane", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Blacrock"), "Blackrock", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Carrgaline"), "Carrigaline", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Carriagline"), "Carrigaline", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Carraigaline"), "Carrigaline", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Carriganara"), "Ballincollig", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Carriganarra"), "Ballincollig", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Carrigrohane"), "Ballincollig", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Caslepark"), "Ballincollig", dataset["locality"])

dataset["locality"] = np.where(dataset["address"].str.contains("Carrigetwohill"), "Carrigtwohill", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Carrightohill"), "Carrigtwohill", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Carrightwohill"), "Carrigtwohill", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Carrigtwohill."), "Carrigtwohill", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Carrigtwhohill"), "Carrigtwohill", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Carrigtoohill"), "Carrigtwohill", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Carrigtohill"), "Carrigtwohill", dataset["locality"])



dataset["locality"] = np.where(dataset["address"].str.contains("Chalreleville"), "Charleville", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Chalreleville"), "Charleville", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Chalreville"), "Charleville", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Charlevile"), "Charleville", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Charlevill"), "Charleville", dataset["locality"])

dataset["locality"] = np.where(dataset["address"].str.contains("Overn"), "Ovens", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Ovesns"), "Ovens", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Owens"), "Ovens", dataset["locality"])


dataset["locality"] = np.where(dataset["address"].str.contains("Blarney"), "Blarney", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Carriagline"), "Carrigaline", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Carraigline"), "Carrigaline", dataset["locality"])
dataset["locality"] = np.where(dataset["address"].str.contains("Carraigaline"), "Carrigaline", dataset["locality"])

#dataset = dataset[dataset["locality"] == ""]












localities = list(dataset["locality_string"].unique())

dataset_cork = dataset[dataset["county"] == "Cork"]
dataset_cork.to_csv("cork_sold_all_3.csv", index=False)


dataset_ballincollig = dataset[dataset["locality"] == "Ballincollig"]


dataset_ballincollig = dataset_ballincollig.drop("locality_string", axis=1)


dataset_ballincollig.to_csv("ballincollig_sold_all.csv", index=False)
















