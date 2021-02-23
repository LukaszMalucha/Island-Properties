# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 20:44:57 2021

@author: LukaszMalucha
"""

import pandas as pd




dataset = pd.read_csv("page-1.csv", encoding="utf-8",header=None)
dataset['pages_list'] = dataset[0].str.split('Page ')




lst = dataset['pages_list'][0]


dataset = pd.DataFrame(lst, columns=["text"])


#######
dataset_problematic = dataset[:1]



dataset = dataset[1:]


#######
dataset_no_proc_num = dataset[~dataset['text'].str.contains('PrcNum')]



dataset = dataset[dataset['text'].str.contains('PrcNum')]

dataset = dataset[0:1]

dataset['text'] = dataset['text'].str.split('PrcNum').str[1]
dataset['text']=dataset['text'].str.replace('PrcShrt','')
dataset['text']=dataset['text'].str.replace('\r',' ')



dataset['text'] = dataset['text'].str.split('\n')



def list_split(lst):
    codes = []
    desc = []
    abr = []
    total_list = []
    for element in lst:
        if '3' in element and '0' in element:
            codes.append(element)
        elif len(element) > 8:
            desc.append(element)
        elif len(element) == 7:
            abr.append(element)
    total_list = [codes, desc, abr]
    return total_list
            
            
    
dataset['new_list'] = dataset['text'].apply(lambda x: list_split(x))












































