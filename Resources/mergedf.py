#Reader for Suicide File
import pandas as pd
from collections import OrderedDict
import numpy as np

# main suicide csv load and clean-up
csv_path = "reviseddata.csv"
suicide_df = pd.read_csv(csv_path, low_memory=False)
suicide_df2 = suicide_df.dropna()
suicide_df2
# happiness df load by year
csv_path = "Happiness_Reports/2015.csv"
happy15_df = pd.read_csv(csv_path, low_memory=False)
csv_path = "Happiness_Reports/2016.csv"
happy16_df = pd.read_csv(csv_path, low_memory=False)
csv_path = "Happiness_Reports/2017.csv"
happy17_df = pd.read_csv(csv_path, low_memory=False)
csv_path = "Happiness_Reports/2018.csv"
happy18_df = pd.read_csv(csv_path, low_memory=False)

# put suffix on columns
happy15_df.columns = happy15_df.columns.map(lambda x: str(x) + "_15")
happy16_df.columns = happy16_df.columns.map(lambda x: str(x) + "_16")
happy17_df.columns = happy17_df.columns.map(lambda x: str(x) + "_17")
happy18_df.columns = happy18_df.columns.map(lambda x: str(x) + "_18")

# merge df's into one
merge_df = pd.merge(suicide_df2, happy15_df, left_on='Country Name',right_on='Country_15', suffixes=('suicide15','happy15'))
merge_df2 = pd.merge(merge_df, happy16_df, left_on='Country Name',right_on='Country_16', suffixes=('suicide16','happy16'))
merge_df3 = pd.merge(merge_df2, happy17_df, left_on='Country Name',right_on='Country_17', suffixes=('suicide17','happy17'))
merge_df4 = pd.merge(merge_df3, happy18_df, left_on='Country Name',right_on='Country or region_18', suffixes=('suicide18','happy18'))

# list of columns to rearrange
pops=[ '2015', '2016', '2017', '2018','Country_15',
 'Region_15',
 'Happiness Rank_15',
 'Happiness Score_15',
 'Standard Error_15',
 'Economy (GDP per Capita)_15',
 'Family_15',
 'Health (Life Expectancy)_15',
 'Freedom_15',
 'Trust (Government Corruption)_15',
 'Generosity_15',
 'Dystopia Residual_15',
 'Country_16',
 'Region_16',
 'Happiness Rank_16',
 'Happiness Score_16',
 'Lower Confidence Interval_16',
 'Upper Confidence Interval_16',
 'Economy (GDP per Capita)_16',
 'Family_16',
 'Health (Life Expectancy)_16',
 'Freedom_16',
 'Trust (Government Corruption)_16',
 'Generosity_16',
 'Dystopia Residual_16',
 'Country_17',
 'Happiness.Rank_17',
 'Happiness.Score_17',
 'Whisker.high_17',
 'Whisker.low_17',
 'Economy..GDP.per.Capita._17',
 'Family_17',
 'Health..Life.Expectancy._17',
 'Freedom_17',
 'Generosity_17',
 'Trust..Government.Corruption._17',
 'Dystopia.Residual_17',
 'Overall rank_18',
 'Country or region_18',
 'Score_18',
 'GDP per capita_18',
 'Social support_18',
 'Healthy life expectancy_18',
 'Freedom to make life choices_18',
 'Generosity_18',
 'Perceptions of corruption_18']
cols = list(merge_df4.columns.values)

# pop columns
for col in pops:
       cols.pop(cols.index(col))

#return to correct order
mergedfinaldf = merge_df4[cols+['2015', 'Country_15',
 'Region_15',
 'Happiness Rank_15',
 'Happiness Score_15',
 'Standard Error_15',
 'Economy (GDP per Capita)_15',
 'Family_15',
 'Health (Life Expectancy)_15',
 'Freedom_15',
 'Trust (Government Corruption)_15',
 'Generosity_15',
 'Dystopia Residual_15','2016','Country_16',
 'Region_16',
 'Happiness Rank_16',
 'Happiness Score_16',
 'Lower Confidence Interval_16',
 'Upper Confidence Interval_16',
 'Economy (GDP per Capita)_16',
 'Family_16',
 'Health (Life Expectancy)_16',
 'Freedom_16',
 'Trust (Government Corruption)_16',
 'Generosity_16',
 'Dystopia Residual_16','2017', 'Country_17',
 'Happiness.Rank_17',
 'Happiness.Score_17',
 'Whisker.high_17',
 'Whisker.low_17',
 'Economy..GDP.per.Capita._17',
 'Family_17',
 'Health..Life.Expectancy._17',
 'Freedom_17',
 'Generosity_17',
 'Trust..Government.Corruption._17',
 'Dystopia.Residual_17','2018',
 'Overall rank_18',
 'Country or region_18',
 'Score_18',
 'GDP per capita_18',
 'Social support_18',
 'Healthy life expectancy_18',
 'Freedom to make life choices_18',
 'Generosity_18',
 'Perceptions of corruption_18']]




# individual years
merged2015df = mergedfinaldf.drop(['Total', 'Max', 'Min', 'Avg', '2000', '2001', '2002', '2003', '2004',
       '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
       '2014', '2019', '2016', 'Country_16', 'Region_16',
       'Happiness Rank_16', 'Happiness Score_16',
       'Lower Confidence Interval_16', 'Upper Confidence Interval_16',
       'Economy (GDP per Capita)_16', 'Family_16',
       'Health (Life Expectancy)_16', 'Freedom_16',
       'Trust (Government Corruption)_16', 'Generosity_16',
       'Dystopia Residual_16', '2017', 'Country_17', 'Happiness.Rank_17',
       'Happiness.Score_17', 'Whisker.high_17', 'Whisker.low_17',
       'Economy..GDP.per.Capita._17', 'Family_17',
       'Health..Life.Expectancy._17', 'Freedom_17', 'Generosity_17',
       'Trust..Government.Corruption._17', 'Dystopia.Residual_17', '2018',
       'Overall rank_18', 'Country or region_18', 'Score_18',
       'GDP per capita_18', 'Social support_18', 'Healthy life expectancy_18',
       'Freedom to make life choices_18', 'Generosity_18',
       'Perceptions of corruption_18'],axis=1)
merged2015df.columns = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code',
       '2015_Suicides/100k', 'Country_15', 'Region_15', 'Happiness Rank_15',
       'Happiness Score_15', 'Standard Error_15',
       'Economy (GDP per Capita)_15', 'Family_15',
       'Health (Life Expectancy)_15', 'Freedom_15',
       'Trust (Government Corruption)_15', 'Generosity_15',
       'Dystopia Residual_15']
merged2016df = mergedfinaldf.drop(['Total', 'Max', 'Min', 'Avg', '2000', '2001', '2002', '2003', '2004',
       '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
       '2014', '2019', '2015', 'Country_15', 'Region_15', 'Happiness Rank_15',
       'Happiness Score_15', 'Standard Error_15',
       'Economy (GDP per Capita)_15', 'Family_15',
       'Health (Life Expectancy)_15', 'Freedom_15',
       'Trust (Government Corruption)_15', 'Generosity_15',
       'Dystopia Residual_15', '2017', 'Country_17', 'Happiness.Rank_17',
       'Happiness.Score_17', 'Whisker.high_17', 'Whisker.low_17',
       'Economy..GDP.per.Capita._17', 'Family_17',
       'Health..Life.Expectancy._17', 'Freedom_17', 'Generosity_17',
       'Trust..Government.Corruption._17', 'Dystopia.Residual_17', '2018',
       'Overall rank_18', 'Country or region_18', 'Score_18',
       'GDP per capita_18', 'Social support_18', 'Healthy life expectancy_18',
       'Freedom to make life choices_18', 'Generosity_18',
       'Perceptions of corruption_18'],axis=1)
merged2016df.columns = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code',
       '2016_Suicides/100k', 'Country_16', 'Region_16', 'Happiness Rank_16',
       'Happiness Score_16', 'Lower Confidence Interval_16',
       'Upper Confidence Interval_16', 'Economy (GDP per Capita)_16',
       'Family_16', 'Health (Life Expectancy)_16', 'Freedom_16',
       'Trust (Government Corruption)_16', 'Generosity_16',
       'Dystopia Residual_16']
merged2017df = mergedfinaldf.drop(['Total', 'Max', 'Min', 'Avg', '2000', '2001', '2002', '2003', '2004',
       '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
       '2014', '2019', '2015', 'Country_15', 'Region_15', 'Happiness Rank_15',
       'Happiness Score_15', 'Standard Error_15',
       'Economy (GDP per Capita)_15', 'Family_15',
       'Health (Life Expectancy)_15', 'Freedom_15',
       'Trust (Government Corruption)_15', 'Generosity_15',
       'Dystopia Residual_15', '2016', 'Country_16', 'Region_16',
       'Happiness Rank_16', 'Happiness Score_16',
       'Lower Confidence Interval_16', 'Upper Confidence Interval_16',
       'Economy (GDP per Capita)_16', 'Family_16',
       'Health (Life Expectancy)_16', 'Freedom_16',
       'Trust (Government Corruption)_16', 'Generosity_16',
       'Dystopia Residual_16', '2018',
       'Overall rank_18', 'Country or region_18', 'Score_18',
       'GDP per capita_18', 'Social support_18', 'Healthy life expectancy_18',
       'Freedom to make life choices_18', 'Generosity_18',
       'Perceptions of corruption_18'],axis=1)
merged2017df.columns = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code',
       '2017_Suicides/100k', 'Country_17', 'Happiness.Rank_17', 'Happiness.Score_17',
       'Whisker.high_17', 'Whisker.low_17', 'Economy..GDP.per.Capita._17',
       'Family_17', 'Health..Life.Expectancy._17', 'Freedom_17',
       'Generosity_17', 'Trust..Government.Corruption._17',
       'Dystopia.Residual_17']
merged2018df = mergedfinaldf.drop(['Total', 'Max', 'Min', 'Avg', '2000', '2001', '2002', '2003', '2004',
       '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
       '2014', '2019', '2015', 'Country_15', 'Region_15', 'Happiness Rank_15',
       'Happiness Score_15', 'Standard Error_15',
       'Economy (GDP per Capita)_15', 'Family_15',
       'Health (Life Expectancy)_15', 'Freedom_15',
       'Trust (Government Corruption)_15', 'Generosity_15',
       'Dystopia Residual_15', '2016', 'Country_16', 'Region_16',
       'Happiness Rank_16', 'Happiness Score_16',
       'Lower Confidence Interval_16', 'Upper Confidence Interval_16',
       'Economy (GDP per Capita)_16', 'Family_16',
       'Health (Life Expectancy)_16', 'Freedom_16',
       'Trust (Government Corruption)_16', 'Generosity_16',
       'Dystopia Residual_16', '2017', 'Country_17', 'Happiness.Rank_17',
       'Happiness.Score_17', 'Whisker.high_17', 'Whisker.low_17',
       'Economy..GDP.per.Capita._17', 'Family_17',
       'Health..Life.Expectancy._17', 'Freedom_17', 'Generosity_17',
       'Trust..Government.Corruption._17', 'Dystopia.Residual_17'],axis=1)
merged2018df.columns = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code',
       '2018_Suicides/100k', 'Overall rank_18', 'Country or region_18', 'Score_18',
       'GDP per capita_18', 'Social support_18', 'Healthy life expectancy_18',
       'Freedom to make life choices_18', 'Generosity_18',
       'Perceptions of corruption_18']
mergedfinalfiltered = mergedfinaldf.drop(['2000', '2001', '2002', '2003', '2004',
       '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
       '2014', '2019'],axis=1)
# suicide filtered file
suicide_filtered = suicide_df2.drop(['Total', 'Max', 'Min', 'Avg', '2000', '2001', '2002', '2003', '2004',
       '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
       '2014', '2019'],axis=1)


dflist = ['mergedfinaldf','merged2015df','merged2016df','merged2017df','merged2018df','mergedfinalfiltered','suicide_filtered']

