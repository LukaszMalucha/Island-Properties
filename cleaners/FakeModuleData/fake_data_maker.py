# -*- coding: utf-8 -*-
"""
Created on Wed May 27 14:26:01 2020

@author: LukaszMalucha
"""

import pandas as pd
import numpy as np
import random
from pathlib import Path


letters = "RSTUVWXYZGHI"

def random_part(string):
    num1 = str(random.randint(1,6))
    num2 = str(random.randint(1,6))
    first = random.choice("RSTVWXYHI")
    second = random.choice("RSTVWXYHI")
    return first + second + "-" + num1 + num2 + " " + string
    
a = random_part("module")


def fake_data(data, filename):
    
    dataset = pd.read_csv(data, encoding="utf-8") 
    
    dataset["document_link"] = dataset["document_link"].str.split("\/").str[-1]
    dataset["document_link"] = dataset["document_link"].str.lower()
    dataset["document_link"] = dataset["document_link"].str.replace("0", "")
    dataset["document_link"] = dataset["document_link"].str.replace("1", "")
    dataset["document_link"] = dataset["document_link"].str.replace("2", "")
    dataset["document_link"] = dataset["document_link"].str.replace("3", "")
    dataset["document_link"] = dataset["document_link"].str.replace("4", "")
    dataset["document_link"] = dataset["document_link"].str.replace("5", "")
    dataset["document_link"] = dataset["document_link"].str.replace("6", "")
    dataset["document_link"] = dataset["document_link"].str.replace("7", "")
    dataset["document_link"] = dataset["document_link"].str.replace("8", "")
    dataset["document_link"] = dataset["document_link"].str.replace("9", "")
    dataset["document_link"] = dataset["document_link"].str.replace("~", "")
    dataset["document_link"] = dataset["document_link"].str.replace("a", "")
    dataset["document_link"] = dataset["document_link"].str.replace("o", "")
    dataset["document_link"] = dataset["document_link"].str.replace("e", "")
    dataset["document_link"] = dataset["document_link"].str.replace("i", "")
    dataset["document_link"] = dataset["document_link"].str.replace("u", "")
    dataset["document_link"] = dataset["document_link"].str.replace("y", "")
    dataset["document_link"] = dataset["document_link"].str.replace("_", "")
    dataset["document_link"] = dataset["document_link"].str.replace("b", "")
    dataset["document_link"] = dataset["document_link"].str.replace("c", "")
    dataset["document_link"] = dataset["document_link"].str.replace("d", "")
    dataset["document_link"] = dataset["document_link"].str.replace("f", "")
    dataset["document_link"] = dataset["document_link"].str.replace("g", "")
    
    # COMPANIES
    
    dataset = dataset.replace({'Johnson Controls': 'Septellar'}, regex=True)
    dataset = dataset.replace({'YORK': 'FusionWave'}, regex=True)
    dataset = dataset.replace({'Metasys': 'Sistema'}, regex=True)
    dataset = dataset.replace({'Simplex': 'Accelena'}, regex=True)
    dataset = dataset.replace({'PENN Controls': 'Tekno'}, regex=True)
    dataset = dataset.replace({'Kantech': 'Tekno'}, regex=True)
    dataset = dataset.replace({'Facility Explorer': 'Pathfinder'}, regex=True)
    dataset = dataset.replace({'LUX': 'CraftWarp'}, regex=True)
    dataset = dataset.replace({'CEM Systems': 'Accelena'}, regex=True)
    dataset = dataset.replace({'Exacq': 'Lunarex'}, regex=True)
    dataset = dataset.replace({'Sensormatic': 'Stellaris'}, regex=True)
    dataset = dataset.replace({'BCPro': 'ModuleX'}, regex=True)
    dataset = dataset.replace({'Tyco': 'Astronomo'}, regex=True)
    dataset = dataset.replace({'Quantech': 'Lumaliel'}, regex=True)
    dataset = dataset.replace({'Autocall': 'Lumaliel'}, regex=True)
    dataset = dataset.replace({'FIREATER': 'Accelena'}, regex=True)
    dataset = dataset.replace({'Fraser-Johnston': 'Accelena'}, regex=True)
    dataset = dataset.replace({'HYGOOD': 'Tekno'}, regex=True)
    dataset = dataset.replace({'PYRO CHEM': 'Tekno'}, regex=True)
    dataset = dataset.replace({'Luxaire': 'Tekno'}, regex=True)
    dataset = dataset.replace({'Coleman': 'Tekno'}, regex=True)
    dataset = dataset.replace({'LUX': 'Sistema'}, regex=True)
    dataset = dataset.replace({'Ruskin': 'CraftWarp'}, regex=True)
    dataset = dataset.replace({'SABO FOAM': 'CraftWarp'}, regex=True)
    dataset = dataset.replace({'SKUM': 'CraftWarp'}, regex=True)
    dataset = dataset.replace({'Triatek': 'CraftWarp'}, regex=True)
    dataset = dataset.replace({'TrueVUE': 'Accelena'}, regex=True)
    dataset = dataset.replace({'WILLIAMS': 'Accelena'}, regex=True)
    dataset = dataset.replace({'Zettler': 'Accelena'}, regex=True)
    dataset = dataset.replace({'THORN SECURITY': 'Accelena'}, regex=True)
    dataset = dataset.replace({'CHEMGUARD': 'FusionWave'}, regex=True)
    dataset = dataset.replace({'Champion': 'FusionWave'}, regex=True)
    dataset = dataset.replace({'Frick': 'FusionWave'}, regex=True)
    dataset = dataset.replace({'ANSUL': 'FusionWave'}, regex=True)
    dataset = dataset.replace({'LPG': 'FusionWave'}, regex=True)
    dataset = dataset.replace({'NEURUPPIN': 'FusionWave'}, regex=True)
    dataset = dataset.replace({'PEAK': 'FusionWave'}, regex=True)
    dataset = dataset.replace({'ShopperTrak': 'FusionWave'}, regex=True)
    dataset = dataset.replace({'TempMaster': 'FusionWave'}, regex=True)
    dataset = dataset.replace({'Verasys': 'FusionWave'}, regex=True)
    dataset = dataset.replace({'GEM': 'Pathfinder'}, regex=True)
    dataset = dataset.replace({'Not Specified': 'Pathfinder'}, regex=True)
    
    # DOCUMENTS
    
    
    #dataset = dataset[dataset['brand'] == "Septellar"]
    
    dataset['document_title'] = np.where((dataset['document_title'].str.contains("Bulletin")), "Ship Module", dataset['document_title'])
    dataset['document_title'] = np.where((dataset['document_title'].str.contains("Glossary")), "Rocket Booster", dataset['document_title'])
    dataset['document_title'] = np.where((dataset['document_title'].str.contains("Manual")), "Crew Facilities", dataset['document_title'])
    dataset['document_title'] = np.where((dataset['document_title'].str.contains("Instruction")), "External Tank", dataset['document_title'])
    dataset['document_title'] = np.where((dataset['document_title'].str.contains("Wizard")), "Fuel Pod", dataset['document_title'])
    dataset['document_title'] = np.where((dataset['document_title'].str.contains("Appendix")), "Life Support", dataset['document_title'])
    dataset['document_title'] = np.where((dataset['document_title'].str.contains("Note")), "Navigation AI", dataset['document_title'])
    dataset['document_title'] = np.where((dataset['document_title'].str.contains("Guide")), "Gascogine-12", dataset['document_title'])
    dataset['document_title'] = np.where((dataset['document_title'].str.contains("Catalog")), "Space Lift", dataset['document_title'])
    dataset['document_title'] = np.where((dataset['document_title'].str.contains("Release")), "Space Storage", dataset['document_title'])
    dataset['document_title'] = np.where((dataset['document_title'].str.contains("What")), "Moon Lander", dataset['document_title'])
    dataset['document_title'] = np.where((dataset['document_title'].str.contains("License")), "Vegetation Kit", dataset['document_title'])
    dataset['document_title'] = np.where((dataset['document_title'].str.contains("Datasheet")), "Mining Equipment", dataset['document_title'])
    dataset['document_title'] = np.where((dataset['document_title'].str.contains("Data Sheet")), "Mining Equipment", dataset['document_title'])
    dataset['document_title'] = np.where((dataset['document_title'].str.contains("Specifications")), "Storage Module", dataset['document_title'])
    dataset['document_title'] = np.where((dataset['document_title'].str.contains("Packing")), "Cooling Systems", dataset['document_title'])
    dataset['document_title'] = np.where((dataset['document_title'].str.contains("Reference")), "Docking Station", dataset['document_title'])
    dataset['document_title'] = np.where((dataset['document_title'].str.contains("Unit")), "Exploration Drones", dataset['document_title'])
    dataset['document_title'] = np.where((dataset['document_title'].str.len() > 14), "Base Module", dataset['document_title'])

    
    # TOPICS
    dataset['topic_title'] = np.where((dataset['document_link'].str.len() == 5), "Software Integration", dataset['topic_title'])
    dataset['topic_title'] = np.where((dataset['document_link'].str.len() == 6), "Conceptual Design", dataset['topic_title'])
    dataset['topic_title'] = np.where((dataset['document_link'].str.len() == 7), "Preliminary design phase", dataset['topic_title'])
    dataset['topic_title'] = np.where((dataset['document_link'].str.len() == 8), "Detail design phase", dataset['topic_title'])
    dataset['topic_title'] = np.where((dataset['document_link'].str.len() == 9), "Re-engine", dataset['topic_title'])
    dataset['topic_title'] = np.where((dataset['document_link'].str.len() == 10), "Risk and reliability", dataset['topic_title'])
    dataset['topic_title'] = np.where((dataset['document_link'].str.len() == 11), "Experimental Testing", dataset['topic_title'])
    dataset['topic_title'] = np.where((dataset['document_link'].str.len() > 11), "Production", dataset['topic_title'])
    
    
    
    dataset['topic_title'] = dataset['document_title'].apply(lambda x: random_part(x))
    
    
    
    
    
    dataset = dataset[dataset['document_title'].str.len() < 18 ]
    
    
    

    
    
    
    dataset["module_link"] = dataset["document_link"] 
    
    dataset["file_type"] = np.where((dataset['file_type'] == "html"), "Ground", dataset["file_type"]) 
    dataset["file_type"] = np.where((dataset['file_type'] == "pdf"), "Orbit", dataset["file_type"]) 
    
    
    dataset["budget"] = dataset["char_total"]
    dataset['module_title'] = dataset['document_title']
    dataset['phase_title'] = dataset['topic_title']
    
    
    dataset = dataset.drop(["char_total"], axis = 1)

    dataset = dataset.drop(["document_link"], axis = 1)
    dataset = dataset.drop(["document_title"], axis = 1)
    dataset = dataset.drop(["topic_title"], axis = 1)
    
    
    
    title = random_part("D")
    
    dataset.to_csv(filename + title + ".csv",  encoding="utf-8-sig", index=False)
    
    return dataset











CSV = list(Path.cwd().glob('*.csv'))

CSV_FILES = [str(Path(filename).stem) for filename in CSV]


    
def fake_it(CSV):
    
    for file in CSV:
        filename = (str(Path(file).stem))
        fake_data(file, filename)    
    
    
fake_it(CSV)    










