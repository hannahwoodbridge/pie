# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 10:15:07 2018

@author: daoud
"""

import pandas as pd
import numpy as np
import csv

def write_output_file(df, index_rapport, nom_fichier):
    with open(nom_fichier+'.csv', mode='w') as csv_file:
        fieldnames = ['Id', 'Rapport']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for k in range(4):
            writer.writerow({'Id': int(df[k][0]), 'rapport': df[4]})