import numpy as np
import pandas as pd
from decimal import *
import re
cityData = pd.read_csv('resources/texas-cities.csv', delimiter = ',')
countyData = pd.read_csv('resources/cities-to-county.csv', delimiter = ',')

# Strip 'name' col into two new cols 'name' & 'state'
cityData[['name','state']] = cityData['name'].str.split(',',expand=True)

# Split leftover 'name' and create city type col with last word from each row
cityData["citytype"] = cityData["name"].str.split().str[-1]

# Group Each city type in its own DF
cityGroup = cityData[cityData.citytype =='city']
townGroup = cityData[cityData.citytype =='town']
villageGroup = cityData[cityData.citytype =='village']



# NUMBER ONE - ***************************************************************
# :What was the largest city, town, and village in each year?
# -> [year, cityName, townName, villageName] x8
# Sort by values in first year for each group 
p=1
for year in cityGroup:
#     print (p)
    cityGroupMax = cityGroup.sort_values(by=['2010'], ascending=False).head(1)
    townGroupMax = townGroup.sort_values(by=['2010'], ascending=False).head(1)
    villageGroupMax = villageGroup.sort_values(by=['2010'], ascending=False).head(1)
    p=p+1
#     print(year, cityGroupMax.iloc[0, 0], townGroupMax.iloc[0,0], villageGroupMax.iloc[0,0]) # ANSWER

    #     TODO: iterate the sort by year to the loop index and have it sort every loop by new col
# Uncomment these to check Dataframes for sorted values of each group
# print(cityGroupMax)
# print(townGroupMax)
# print(villageGroupMax)


# NUMBER TWO - ***************************************************************
# :Get the 3 fastest growing cities in texas bw 2012-2016

# calculate difference between end year and start year save to new column
cityData['citygrowth'] = cityGroup['2016']-cityGroup['2012']
# sort max list descending order return top 3 rows
growthSorted = cityData.sort_values(by=['citygrowth'], ascending=False).head(3)
# Save names of cities to list
fastestGrowingCities = growthSorted[['name']]

print('#2) The Fastest growing cities in Texas were:')
print(growthSorted['name'])  # ANSWER


# NUMBER SIX - ***************************************************************
# :What percentage of Texans lived in towns in 2017?
# -> [townsPercent %]

# Get totalPopulation
pop17 = cityData['2017'].sum()
# Get totalPopulationTowns
popTown17 = townGroup['2017'].sum()
# typecast to float and get Percentage
townPercent = Decimal(popTown17) / Decimal(pop17) *100
# Return Formatted Percentage of Town
print ('#6)  '+'{0:.2f}'.format(townPercent) +'% of Texans lived in Towns in 2017') # ANSWER




# NUMBER SEVEN - ***************************************************************
# :Which year did Texas grow the most?
# -> [year]


# Sum all rows to bottom of dataframe
cityData.loc['totals'] = cityData.sum()

# Calc percent change between total row and the highest number in dataframe row as a percentage
maxGrowth = cityData.loc['totals', '2010':'2017'].pct_change().max()*100

largestGrowthYear = cityData.loc['totals', '2010':'2017'].pct_change().idxmax()

# Print Percentage value and Year
print ('#7) At'+' {0:.2f}'.format(maxGrowth)+' %,' + ' '+ largestGrowthYear + ' was the largest growth year in Texas') # ANSWER




# NUMBER THREE - ***************************************************************
# :Which county had the most population in each year?
# -> [year, countyName] x8

# Sort countyData by 'CITY' and remove duplicates
countyData = countyData.sort_values(by=['CITY']).drop_duplicates(['CITY'])

#Get first word as the city name
cityData['CITY'] = cityData["name"].str.split().str[0] 
# cityData2.tail()
# countyData.tail()




# Group by 'COUNTY'
# get totalCountyPop per county in countyGroup

# # Group by county
# CountyGroup = frame[frame.COUNTY =='COUNTY']
# Get the maximum (returns a countyname and year)
# # CountyGroup.max()




countyData.merge(cityData, how='left', left_on='CITY', right_on='CITY').head()