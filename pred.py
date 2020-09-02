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

