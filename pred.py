# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 23:10:17 2020

@author: sarth
"""

#Importing necessary Header files 

import pandas as pd
import numpy as np
import math
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

#Importing Data 
df = pd.read_excel("Data_Train.xlsx")


df.head()
df.shape
df.info()



'''mileage = df[df['Mileage']].apply ( lambda x: x.split(' ')[0])'''


""" MILEAGE """
# removing the units from mileage 
def setmileage(daf):
    d = str(daf.Mileage).split(" ")[0]
    return float(d)

df["Mileage"] = df.apply(setmileage, axis=1)

#Filling null values 
df['Mileage'].fillna(df['Mileage'].median(), inplace=True)

#Remvoing all 0 fig outliers
df = df[df.Mileage != 0]




"""   ENGINE   """
# removing the units from engine
def setengine(daf):
    d = str(daf.Engine).split(" ")[0]
    return float(d)

df["Engine"] = df.apply(setengine, axis=1)

#Filling null values 
df['Engine'].fillna(df['Engine'].mean(), inplace=True)



"""    POWER     """
#Removing 
def setpower(daf):
    d = str(daf.Power).split(" ")[0]
    if d == "null":
        pass
    else:
        return float(d)

df["Power"] = df.apply(setpower, axis=1)

df['Power'].fillna(df['Power'].median(), inplace=True)

"""     SEATS      """

df=df.dropna()




