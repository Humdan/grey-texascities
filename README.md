Texas Cities Data Ingestor
Humdan Bakhshi
Sept 26,2018

Grey Inc - Interview Exam

Criteria:
All questions must be answered programmatically

Questions:
1) What was the largest city, town, and village in each year?
2) What are the three fastest growing cities in Texas between 2012-2016?
3) Which county had the most population in each year?
4) Which county experienced the most growth in population over the timespan?
5) Which county experienced the highest rate of growth from 2014-2016?
6) What percentage of Texans lived in towns in 2017?
7) Which year did Texas grow the most?


Tools Used:
	Jupyter Notebook IDE

Libraries:
	Pandas
	Redux
	Pathlib

_____________________________________________________________________

HOW TO RUN

navigate to project root folder

double click 'run.sh' 
OR from terminal:
./run.sh

OR run individual files

python <filename>.py


_____________________________________________________________________
VERSION LOG

0.1	Using mainly core python functions and string arithmetic to group dataframes within grouplist
Needed to make my own column headers and setup individual for loops for every enumerate call
This took way too long and I was only able to answer question 1 and was not the most elegant of solutions
I'm not sure if the answer is right though, since they all appreared to be the same.
My code in this first version is not easy to troubleshoot.  I know I'll need to make some simplifications if this is all going to work together with minimal code.
Started watching some Pandas videos

0.2 Decided to approach the problems cumulatively and searched for functions that could overlap.  Its best to know what each function is evolving to and how it may be used in other areas of the test
parsing each population year into an array var helped keep easy access to the original data frame
Grouped by cityType to SAC .max() function from each group
For loop to reiterate the max() function from each group for every year
More Pandas videos and a tutorial

0.3 This approach is by far the most elegant one where it simply manipulates dataframes, groups them, and applies arithmetic.  This approach will cover most other functions to derive the appropriate dataframes for each operation.. if there's time left..

