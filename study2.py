# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 08:03:37 2019

@author: dcamp
"""

# Import the pandas package
import pandas as pd

# Initialize reader object: df_reader
df_reader = pd.read_csv('ind_pop.csv', chunksize=10)

# Print two chunks
print(next(df_reader))
print(next(df_reader))
