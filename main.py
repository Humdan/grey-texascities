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

print("#1)  The largest city, town, and village in each year were")
for year in cityGroup:
#     print (p)
    cityGroupMax = cityGroup.sort_values(by=['2010'], ascending=False).head(1)
    townGroupMax = townGroup.sort_values(by=['2010'], ascending=False).head(1)
    villageGroupMax = villageGroup.sort_values(by=['2010'], ascending=False).head(1)
    p=p+1
    print(year, cityGroupMax.iloc[0, 0], townGroupMax.iloc[0,0], villageGroupMax.iloc[0,0]) # ANSWER

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



# NUMBER THREE - ***************************************************************
# :Which county had the most population in each year?
# -> [year, countyName] x8

# Sort countyData by 'CITY' and remove duplicates
countyData = countyData.sort_values(by=['CITY']).drop_duplicates(['CITY'])
# Cleanup County Data
countyData.COUNTY = countyData.COUNTY.str.replace('^ +', '')
countyData.CITY = countyData.CITY.str.replace('^ +', '')

# Get fresh copy of original City CSV file
cityData2 = pd.read_csv('resources/texas-cities.csv', delimiter = ',')
# Strip 'name' col into two new cols 'name' & 'state'
cityData2[['name','state']] = cityData2['name'].str.split(',',expand=True)
#Get first word as the city name
cityData2['CITY'] = cityData2["name"].str.split().str[0] 
        # TODO:  I think this leaves out all the cities with multiple words in the name
cityData2['CITY'] = map(lambda x: x.upper(), cityData2['CITY'])
cityFrame = cityData2[['CITY', '2010','2011', '2012','2013','2014','2015','2016','2017']].copy()

# Combine both dataframes by City Column
frame = countyData.merge(cityFrame, on='CITY', how='outer')
# Group by 'COUNTY'
countyPop = frame.groupby('COUNTY').sum()

# Get the maximum (returns a countyname and year) 
# x = frame.sort_values(by=['2010'], ascending=False).head(1)
print ("#3)  The Largest Counties were:")
for col in (frame.columns):
    # Skip columns that are not a year to do the math
    if col == 'COUNTY' or col == 'CITY':
        print("")        
    else: 
        # Sort current column by highest to lowest and read only one row
        x = frame.sort_values(by=[col], ascending=False).head(1)
        print(col, str(x[['COUNTY']]))                                          #   ANSWER




# NUMBER FOUR - ***************************************************************
# :Which county experienced the most growth in population over the timespan?
# -> [countyName]

# Get the total growth between the years
# Sort by highest to lowest
# Get highest growth county
# Print countyname

frame['GROWTH'] = frame['2017']-frame['2010']



countyGrowthSorted = frame.sort_values(by='GROWTH', ascending=False).head(1)

mostGrowthCounty = countyGrowthSorted.iloc[0,0]

print("#4)  The county that experienced the most growth in population was " + mostGrowthCounty +"County") #   ANSWER



# NUMBER FIVE - ***************************************************************
# :Which county experienced the highest rate of growth from 2014-2016?
# -> [countyName]
frame['GROWTH2'] = frame['2016']-frame['2014']

countyGrowthSorted2 = frame.sort_values(by='GROWTH2', ascending=False)
countyGrowthSorted2.head(1)


mostGrowthCounty2 = countyGrowthSorted.iloc[0,0]
print("#5)  The county that experienced the most growth b/w 2014-2016 was " + mostGrowthCounty2 +"County") #   ANSWER



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








