# project1
Repo for Project one

Link to suicide data:https://data.worldbank.org/indicator/SH.STA.SUIC.P5


Code to merge and format dataframes is located in mergedf.py file. All you need to do is paste this code into the first box of any notebook and hit shift enter and it should import and merge the csv's.

I have been running all my tests in the Merged_DataFrame.ipynb notebook by running the first block and then doing subsequent analysis on those df's

Once you run the code, you can enter:
dflist

This will give you a current list of the dataframes I have created.

The top level, full detail data frame for us is:
mergedfinalfiltered

That DF contains 2015-2018 data for suicides merged with those years' Happiness index info. 

If you want just suicide data for 2015-2018:
suicide_filtered
