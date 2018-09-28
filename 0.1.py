import os
import pandas as pd
import pathlib


file1 = "texas-cities.csv"
file2 = "cities-to-county.csv"
savename = "maxPlace.csv" #Change to desired file name

#Assigns the path ; change to relative path so it can be run anywhere
root = os.path.join(os.path.join(os.path.expanduser('~')), '/Users/h/documents/dev/_prj/grey/resources/')

citydf = pd.read_csv(open(root + file1,"rb"), index_col=False) # read citydata file as dataframe
countydf = pd.read_csv(open(root + file2,"rb"), index_col=False)  #read counties file as dataframe


# Create Individual Lists
groupList = ["city", "town", "village"]
yearList = ["2010","2011","2012","2013","2014","2015","2016","2017"]
maxList = []
placeList = []
countyList = []

for x in groupList:
    group = citydf[citydf['name'].str.contains(" %s" % x)] #creates abbreviated dataframe with places from either cities, towns, or villages, determined by loop
    for y in yearList:
        maxList.append(max(group[y])) #appends to List max value for place in a specific year, determined by loop
        placeList.append(group.loc[group[y] == max(group[y]), 'name'].iloc[0]) #appends to List name of place for a specific year, determined by loop

d = pd.DataFrame({"Results": ["Name", "Size"]}) #first column of new dataframe

for i, x in enumerate(placeList[0:8]):
    countyList.append(countydf.loc[countydf["CITY"] == " "+placeList[i].split(" ", 1)[0].upper(), "COUNTY"].iloc[0]) #for top cities, locate the associated county

columnList = ["City-2010","City-2011","City-2012","City-2013","City-2014","City-2015","City-2016","City-2017",
             "Town-2010","Town-2011","Town-2012","Town-2013","Town-2014","Town-2015","Town-2016","Town-2017",
             "Village-2010","Village-2011","Village-2012","Village-2013","Village-2014","Village-2015","Village-2016","Village-2017"]     

for i, x in enumerate(columnList):
    d[x] = [placeList[i],maxList[i]] #add columns to new dataframe for cities, towns, and villages

countycolumnList = ["County-2010","County-2011","County-2012","County-2013","County-2014","County-2015","County-2016","County-2017"]

for i, x in enumerate(countycolumnList):
    d[x] = [countyList[i],maxList[i]] #add columns to new dataframe for counties

for i, x in enumerate(yearList):
    print [x, d.iat[0,1+i], d.iat[0,9+i], d.iat[0,17+i]]

