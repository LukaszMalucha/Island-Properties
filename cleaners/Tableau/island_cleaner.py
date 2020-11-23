# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 16:48:31 2020

@author: LukaszMalucha
"""

import pandas as pd
import numpy as np


dataset_sale = pd.read_csv("properties.csv", encoding="utf-8")
dataset_rent = pd.read_csv("island_rent.csv", encoding="utf-8")

dataset_sale["locality"] = dataset_sale["locality"].str.replace(" De ", " de ")
dataset_sale["locality"] = dataset_sale["locality"].str.replace(" Del ", " del ")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("ü", "u")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("á", "a")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("ó", "o")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("Cala D'or", "Cala d'Or")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("Granadilla de Abona", "Granadilla")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("Granadilla", "Granadilla de Abona" )
dataset_sale["locality"] = dataset_sale["locality"].str.replace("Palma de Majorca", "Palma de Mallorca")
dataset_sale["locality"] = dataset_sale["locality"].str.replace(" La ", " la ")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("Sa Coma (Cala Millor)", "Sa Coma")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("San Francisco Javier (Arrecife)", "Arrecife")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("í", "i")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("Santa Maria de Guia de Gran Canaria", "Santa Maria de Guia")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("Valsequillo (Telde)", "Valsequillo de Gran Canaria")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("Sa Coma (Cala Millor)", "Sa Coma")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("San Bartolomé de Tirajana", "San Bartolome de Tirajana")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("San Bartolome de Lanzarote", "San Bartolomé")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("San Bartolomé", "San Bartolome de Lanzarote")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("à", "a")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("ÃŒ", "u")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("Ãº", "u")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("Ã±", "n")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("Ã", "a")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("ó", "o")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("Ã", "a")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("Ã§", "c")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("Ã ", "a")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("Ã©", "e")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("Ã³", "o")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("Ã", "i")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("Ã", "i")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("a³", "o")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("a¡", "a")
dataset_sale["locality"] = dataset_sale["locality"].str.replace("S'illot-Cala Morlanda", "S'Illot")



dataset_rent["locality"] = dataset_rent["locality"].str.replace(" De ", " de ")
dataset_rent["locality"] = dataset_rent["locality"].str.replace(" Del ", " del ")
dataset_rent["locality"] = dataset_rent["locality"].str.replace("ü", "u")
dataset_rent["locality"] = dataset_rent["locality"].str.replace("á", "a")
dataset_rent["locality"] = dataset_rent["locality"].str.replace("ó", "o")
dataset_rent["locality"] = dataset_rent["locality"].str.replace("Cala D'or", "Cala d'Or")
dataset_rent["locality"] = dataset_rent["locality"].str.replace("Granadilla de Abona", "Granadilla")
dataset_rent["locality"] = dataset_rent["locality"].str.replace("Granadilla", "Granadilla de Abona" )
dataset_rent["locality"] = dataset_rent["locality"].str.replace("Palma de Majorca", "Palma de Mallorca")
dataset_rent["locality"] = dataset_rent["locality"].str.replace(" La ", " la ")
dataset_rent["locality"] = dataset_rent["locality"].str.replace("Sa Coma (Cala Millor)", "Sa Coma")
dataset_rent["locality"] = dataset_rent["locality"].str.replace("San Francisco Javier (Arrecife)", "Arrecife")
dataset_rent["locality"] = dataset_rent["locality"].str.replace("í", "i")
dataset_rent["locality"] = dataset_rent["locality"].str.replace("Santa Maria de Guia de Gran Canaria", "Santa Maria de Guia")
dataset_rent["locality"] = dataset_rent["locality"].str.replace("Valsequillo (Telde)", "Valsequillo de Gran Canaria")
dataset_rent["locality"] = dataset_rent["locality"].str.replace("Sa Coma (Cala Millor)", "Sa Coma")
dataset_rent["locality"] = dataset_rent["locality"].str.replace("San Bartolomé de Tirajana", "San Bartolome de Tirajana")
dataset_rent["locality"] = dataset_rent["locality"].str.replace("San Bartolome de Lanzarote", "San Bartolomé")
dataset_rent["locality"] = dataset_rent["locality"].str.replace("San Bartolomé", "San Bartolome de Lanzarote")
dataset_rent["locality"] = dataset_rent["locality"].str.replace("à", "a")


sale_localities = list(dataset_sale["locality"].unique())
rent_localities = list(dataset_rent["locality"].unique())



dataset_sale.to_csv("properties.csv", encoding="utf-8")
dataset_rent.to_csv("island_rent.csv", encoding="utf-8", index=False)





