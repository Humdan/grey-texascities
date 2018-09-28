import numpy as np
import re
import pandas as pd
import csv


# IMPLEMENTING PANDAS LIBRARY


df = pd.read_csv('resources/texas-cities.csv', index_col=None)
df.head()

# NUMBER 1 
# Split the column using , delimiter and create "STATE" col
df[['name','state']] = df['name'].str.split(',',expand=True)

# Split again with cityType Filter and create "CITYTYPE" col
df[['type']] = df['name'].str.split("",expand=True)

# Split one more time and extract last word in col
# df[['citytype']] = df[['citytype']].split("",expand=True)
# print(df[['citytype']])




# df['citytype'].split(" ")[:-1]
# cityType.split("")[:-1]
# df['citytype'] = df[['name']].split(" ")

# Extract only last word containing cityType string
# df['citytype'].str.contains('city', regex=True)  #checks and returns bool of whether col contains txt
# df3['citytype'] = df['name'].str.extract('city', expand=True)
# df3['citytype'] = df.composers.str.split('\s+').str[-1]



# Group list by cityType in objectType
# g = df.groupby('citytype')
# Find max per group in first year

# Repeat for each year



# Finds Max value in specific column
# x = cityGroup(df.iloc[:,7].max() #temporarily store as variable


# Print Results  [year, cityName, townName, villageName] x8
# for col in 
#     print(year, cityName, townName, villageName)














# df2['type'].str.split(' ')[:-1]




