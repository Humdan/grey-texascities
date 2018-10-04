PSEUDOCODE:



Data is divided into two databases ( csv files)
Questions must be answered using the cities.csv file
and then referenced from the counties.csv file to answer appropriately to most questions

Tools to build:
read csv
Get each column parsed as a set
Get Max of each set
Reference second csv

Intent:
build as much reusable code as possible
not necessarily built within a function, but nested enough to be able to pick and place




1) What was the largest city, town, and village in each year?
-> [year, cityName, townName, villageName] x8
create separate lists for each dataframe
Split State from 'name' col
Slice last word from remaining 'name' col as 'type'
Group by 'type'
type.typeName.max() + print corresponding cityName

return [year, cityName, townName, villageName] x8
	repeat for all years


2) What are the three fastest growing cities in Texas between 2012-2016?
-> [cityName, cityName, cityName]
index all populations between startYear, and endYear
calculate differences for each ; store to Array
Re order differences array from highest to lowest
reference cityName
return cityName 
	repeat 2 more times


3) Which county had the most population in each year?
-> [year, countyName] x8
Get county DF
Split cityname column again
Add cities data to county DF
	
	OR iloc[0] (first word) in 'name' list to find city name
	match city name to 'City' col in county DF
	-> countyCitySorted[]

Group by 'COUNTY'

Apply
	Get sum of each group per year as a new dataframe countyPop[]
	get Max in each YEAR column of each grouped dataframe 
	print result repeat for next year x8

County , cityname, 


calculate max ; store to var
reference cityName
lookup cityName in counties.csv
return countyName
increment currentYear by 1
	repeat for next year 7 more times


4) Which county experienced the most growth in population over the timespan?
-> [countyName]
group cities to Counties per year
index startYear, endYear populations
calculate differences for each
determine max ; store to var
lookup cityName in counties.csv
return countyName


5) Which county experienced the highest rate of growth from 2014-2016?
-> [countyName]
group county with cityGroup
no multi-return loop ; instead lookup cityName in counties.csv
return countyName


6) What percentage of Texans lived in towns in 2017?
-> [townsPercent %]
	1 Get totalPopulation 
index all city populations in 2017
calculate Sum ; store to var
	2 Get townsPopulation
index all cityName variables
discriminate to those marked 'town' in line starts
index new list of townPopulations
calculate Sum ; store to var
	3 Get townsPercent
 townsPopulation / totalPopulation == townsPercent


7) Which year did Texas grow the most?
-> [year]

group all populations in each year col & sum 
Calculate differences between each year ; store to differenceArray len= 7
	2 Get Year
Determine highest number in differenceArray
Reference year + 1 ( to reference the right side of the difference range)
return year








