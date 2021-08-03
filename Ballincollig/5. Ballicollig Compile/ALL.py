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


dataset["number"] = dataset["address"].str.split(" ").str[0]
dataset["number"] = dataset["number"].str.replace(",", "")

dataset["lat"] = np.where(dataset["area"] == "Old Quarter", "51.89120011526423", dataset["lat"])
dataset["long"] = np.where(dataset["area"] == "Old Quarter", "-8.597460712163135", dataset["long"])


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
dataset["matcher"] = dataset["matcher"].str.replace("Caisleé", "Caisleán")
dataset["matcher"] = dataset["matcher"].str.replace("Caislean", "Caisleán")
dataset["matcher"] = dataset["matcher"].str.split(" ").str[1]

dataset["duplicate"] = dataset.duplicated(subset=['matcher', 'price', 'number', 'area'])



dataset = dataset[dataset["duplicate"] == False]
dataset = dataset.drop(["duplicate", "geocode", "matcher", "number"], axis=1)

dataset["price_per_meter"] = dataset["price"] / dataset["size"]
dataset["price_per_bedroom"] = dataset["price"] / dataset["beds"]



dataset.to_csv("_ballincollig_full_offers.csv", index=False)




"""
POPULARITY
"""




dataset = pd.read_csv("ballincollig_offers_2021.csv", encoding="utf-8")
dataset["date"] = dataset["date"].str.replace("Jul-26-2021", "2021-07-26")

dataset = dataset[["address", "date","popularity"]]



dataset_dates = dataset.pivot(index="address", columns="date", values="popularity")

dataset_dates = dataset_dates.fillna(0)


dataset_dates.to_csv("_ballincollig_popularity.csv")






"""
PRICE COMPARISON
"""


dataset_sold = pd.read_csv("ballincollig_sold.csv", encoding="utf-8")

dataset_sold = dataset_sold[['area', 'address', 'full_address', 'number', 'price', 'date']]


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

dataset_matcher["price_difference"] = (dataset_matcher["price_sold"] - dataset_matcher["price"]) / dataset_matcher["price"]

dataset_matcher["year"] = dataset_matcher["date"].str.split("-").str[0]

dataset_avg_price_difference = dataset_matcher.groupby(["area", "year"])["price_difference"].mean()
dataset_avg_price_difference = dataset_avg_price_difference.reset_index()

#dataset_matcher = dataset_matcher.merge(dataset_avg_price_difference, on="year", how="left")
dataset_matcher = dataset_matcher.drop("year", axis=1)
#dataset_matcher = dataset_matcher.rename(columns={""})

dataset_matcher.to_csv("ballincollig_compare_prices.csv", index=False)





dataset_sold["year"] = dataset_sold["date"].str.split("-").str[0]

dataset_sold = dataset_sold.merge(dataset_avg_price_difference, how="left", on=["year", "area"])
dataset_sold = dataset_sold.rename(columns={"price_difference":"annual_average_price_difference"})







dataset_sold["geocode"] = ""



dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Maglin", "51.88135112776452, -8.59523805920491",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Classis Lake", "51.88586099008718, -8.62822296864587",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Old Quarter", "51.89114003596089, -8.59633561033392",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "The Cloisters", "51.88453436126935, -8.578140286193113",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "West Village", "51.886701875920906, -8.606268807280973",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "The Maltings", "51.88503727921537, -8.591352822622822",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Coolroe", "51.885279789132504, -8.622716969745719",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "An Caislean", "51.88419579207018, -8.604721941977742",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Parknamore", "51.88458744794133, -8.609309161051812",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Castle Road", "51.88237120146108, -8.598641786193197",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Muskerry Estate", "51.885514844369936, -8.596310161258103",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Old Fort Road", "51.88988509759098, -8.59066895920469",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Highfield Park", "51.88438631124541, -8.574891410855766",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Westcourt", "51.88681255417706, -8.616295628522487",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Greenfield", "51.87768330900382, -8.61608163310892",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Castlepark", "51.88650616536384, -8.58533217454591",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Rosewood", "51.88865181082447, -8.575978970851866",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "The Willows", "51.89301140145297, -8.581593590126793",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Town Center", "51.8878563321983, -8.600737381727024",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Carriglee", "51.89320554364949, -8.582261828522315",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Carrigrohanebeg", "51.89309917070151, -8.580849757357647",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Limeworth", "51.88244387440602, -8.582059330369558",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "West Village", "51.88656943500571, -8.60609714591646",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "The Quadrants", "51.8890702782036, -8.589706799326772",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "The Stables", "51.88380436406558, -8.622683203381243",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Leo Murphy Terrace", "51.888591280385164, -8.583440501534145",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Aylsbury", "51.88284449037205, -8.620440916875388",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Wyndham Downs", "51.88595620016782, -8.620113757357807",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Carriganarra", "51.88456579585057, -8.579854607281877",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Hazel Grove", "51.88270220033945, -8.594207045710691",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Cranford Pines", "51.88391871868656, -8.585827588040098",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Beech Park", "51.884462825784524, -8.586660730369518",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Church View", "51.88549636879165, -8.592625889887055",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "The Crescent", "51.88974689003794, -8.592724974545812",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Wyndham Downs", "51.88594295587414, -8.620296147557605",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Tudor Grove", "51.88555121291465, -8.591538215028342",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Westgrove", "51.88676931020199, -8.6146432996872",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Carrigrohane", "51.89608063198051, -8.56348113795949",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Station Cross", "51.88366424957323, -8.588997728522568",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Innishmore", "51.88897474404985, -8.608958999892096",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Powdermills", "51.89225015549648, -8.586096438526356",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Willow Grove", "51.882509982430086, -8.612375401534269",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Castleknock", "51.88198791175574, -8.595112470852024",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Station Road", "51.885856656204545, -8.590996730369481",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Leeview", "51.885856656204545, -8.590996730369481",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Heathfield", "51.88275370396547, -8.57522707085204",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Greystones", "51.88708566318779, -8.572495537963082",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Leesdale Court", "51.89042385266594, -8.583049957357712",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Avoncourt", "51.88515208061713, -8.612719189887075",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Cois Na Cora", "51.89115617169389, -8.586177713181245",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "An Caisleann", "51.89115617169389, -8.586177713181245",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Cois Na Cora", "51.89115617169389, -8.586177713181245",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Fionn Laoi", "51.89295672639931, -8.577244778805012",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Coolroe Meadows", "51.88363432099277, -8.616138226350916",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Greenfields", "51.87941701969475, -8.620193493581136",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Steeplewoods", "51.88978058994379, -8.565944853663783",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Greenfield", "51.88072634468435, -8.611355403381312",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Highfield", "51.88483134751023, -8.573114016875365",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Inniscarra View", "51.88901621244116, -8.572065214668026",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Manor Hill", "51.89121035709487, -8.575907457357648",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Shalimar Court", "51.88896130535807, -8.578969730369383",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Shalimar Court", "51.88896130535807, -8.578969730369383",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "The Cloisters", "51.88453436126935, -8.578108099687265",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Leecourt", "51.8915162277775, -8.581342570851831",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Coolroe Heights", "51.8915162277775, -8.581342570851831",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Daffodil Fields", "51.89114262893351, -8.573402430369397",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Glendower Court", "51.890963893776494, -8.579131855510711",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Mukerry Estate", "51.88554133320571, -8.596438907281483",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Glendower Court", "51.89097713659068, -8.579260601534097",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Glendower Court", "51.89097713659068, -8.579260601534097",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Ovens", "51.88127654707539, -8.658682937965343",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Castle Road", "51.88234227885883, -8.59817565735788",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Carrigrohane", "51.89118108080445, -8.570433423222292",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "West Village", "51.88675485217772, -8.606397553304374",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "West Village", "51.88675485217772, -8.606397553304374",  dataset_sold["geocode"] )
dataset_sold["geocode"] = np.where(dataset_sold["area"] == "Castlepark", "51.88653927567583, -8.585310716875346",  dataset_sold["geocode"] )

dataset_sold = dataset_sold.rename(columns={"address_sold": "address"})
dataset_sold["area"] = dataset_sold["area"].str.strip()

dataset_sold = dataset_sold[dataset_sold["area"] != "Inniscarra"]
dataset_sold = dataset_sold[dataset_sold["area"] != "Ballyburden"]
dataset_sold = dataset_sold[dataset_sold["area"] != "Kilnaglory"]
dataset_sold = dataset_sold[dataset_sold["area"] != "Killumney Road"]
dataset_sold = dataset_sold[dataset_sold["area"] != "Blarney"]
dataset_sold = dataset_sold[dataset_sold["area"] != "Lackenshoneen"]
dataset_sold = dataset_sold[dataset_sold["address"] != "Doire Loin"]
dataset_sold = dataset_sold[dataset_sold["area"] != "Lackenshoneen"]
dataset_sold = dataset_sold[dataset_sold["area"] != "Kerry Pike"]
dataset_sold = dataset_sold[dataset_sold["area"] != "Aherla"]
dataset_sold = dataset_sold[~dataset_sold["address"].str.contains("Grange Hill")]
dataset_sold = dataset_sold[dataset_sold["area"] != "Model Farm Road"]


dataset_sold["lat"] = dataset_sold["geocode"].str.split(", ").str[0]
dataset_sold["long"] = dataset_sold["geocode"].str.split(", ").str[1]


dataset_sold = dataset_sold.drop("geocode", axis=1)





dataset_sold.to_csv("ballincollig_s.csv", index=False)















