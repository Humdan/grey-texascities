import os
import pandas as pd
import numpy as np
import csv



df = pd.read_csv('resources/texas-cities.csv', index_col=None)
df.head()
# print(df.head(1))
num_Cols = len(df.columns)

# parse each column individually as a dataframe
cityNames = df.iloc[:,0].values
pop2010 = df.iloc[:,1].values
pop2011 = df.iloc[:,2].values
pop2012 = df.iloc[:,3].values
pop2013 = df.iloc[:,4].values
pop2014 = df.iloc[:,5].values
pop2015 = df.iloc[:,6].values
pop2016 = df.iloc[:,7].values
pop2017 = df.iloc[:,8].values



# NUMBER 1 

# Bring entire file to memory
# Read through first column


# if last word in name is = 'City or city'
cityGroup = df.groupby('name')
# if last word in name is = 'Town or town'
townGroup = df.groupby('name')
# if last word in name is = 'Village or village'
villageGroup = df.groupby('name')

g = df.groupby('name')

# for name, cityGroup in g:
# 	print(name)
# 	print(cityGroup)

# Individually prints a specific group
print(g.get_group('Adrian city, Texas'))

# Finds Max value in specific column
# x = cityGroup(df.iloc[:,7].max() #temporarily store as variable






#  NUMBER 2
# Get differences & sort the list
growth = np.subtract(df.iloc[:,7].values, df.iloc[:,3].values)
# Append row header name to keep track of which city it is
# Re order array to get first 3 elements
sortedGrowth = sorted(growth, reverse=True) 
fastestGrowths = sortedGrowth[0:3]
# print(fastestGrowths)
# Find each city & print cityNames

pops_2010 = df.groupby('name')




# NUMBER 3
# Read each county into a variable
# Create array of cities in each county
# Determine each city in county arrays
# Determine what cityArray belong in which countyArray



# NUMBER 7
# calculate sum from each year
sum1 = df['2010'].sum()


# calculate difference between each year into array
# find max
# return right side column index header

# for col in df.columns:
# 	# sum of current column with index col
# 	print(df.iloc[:,col].sum)
# 	# save value to array
# 	sums = sums + x
	

# growth1 = np.subtract(pop2010, pop2011)










