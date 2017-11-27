import pandas as pd
import numpy as np

"""
Please find the dataset under data directory
"""
df=pd.read_csv("Landmarks.csv",sep=",")
#print(df.head())
#print(df.groupby('country')['year'].count())
"""
How many records we have?
"""
print(len(df.index))
"""
This is not working
df = pd.read_excel(open('Landmarks.xls','rb'), sheetname='Landmark')
df.head()
"""
#df.columns
"""
The below one will give Top 5 places
Usage
TEMPLE         1021
COMMERCIAL      503
EDUCATIONAL     412
RESIDENTIAL     351
INDUSTRIAL      270
"""
usage_count=df.groupby('Usage')['Name'].count()
print(usage_count.sort_values(axis=0,ascending=False).head())

#print(df.columns)

"""

"""
"""
The below code will give the report Each ward, list of Usage area and its counts
Ward Number  Usage                   
10           COMMERCIAL                   9
             DAILY MARKET                 1
             EDUCATIONAL                  2
             HOSPITAL                     1
             INDUSTRIAL                   9
             OTHERS                       1
11   


12
"""
ward_max_temple=df.groupby(['Ward Number','Usage'])['Usage'].count()
print(ward_max_temple)

"""
Findout Which ward has the maximum Temple
"""
ward_max_temple=df[(df['Usage'] == 'TEMPLE')].groupby(['Ward Number','Usage'])['Usage'].count() 

print(ward_max_temple.sort_values(axis=0,ascending=False).head(5))

"""
is there any missing data?
we can apply isnull function to series only not DF and if whole record is empty only it will return True 1 else False 
"""
print(pd.isnull(df['Ward Number']).value_counts())

"""
Get the Unique values of a column and check for missing Usage area in the ward_max_temple
ex: ward 10 has Temple but ward 11 doesn't. report 11.
"""
print("############################")
unique_usage=list(df.Usage.unique())
print(unique_usage)

wardAndusage=pd.DataFrame(df[['Ward Number','Usage']])
print(type(wardAndusage))

wardAndusageDF=wardAndusage.groupby('Ward Number')['Usage'].unique()
wardAndusageDict=dict(wardAndusageDF)
print(type(wardAndusageDict))

for ward in wardAndusageDict:
    print(ward, end=" ")
    #print(unique_usage not in wardAndusageDict[ward])
    #print([c for c in wardAndusageDict[ward] if c not in unique_usage ])
    print([c for c in unique_usage if c not in wardAndusageDict[ward] ])
    """
    The above and below statements are working and returns same result in different datatypes
    """
    print(set(unique_usage)^set(wardAndusageDict[ward]))
    
