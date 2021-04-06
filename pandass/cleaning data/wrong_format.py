import pandas as pd

wrgdata=pd.read_csv('cleaning data/wrong format.csv')

wrgdata['date']=pd.to_datetime(wrgdata['date'])

print(wrgdata.to_string())
"""
   sno       date
0    1 2021-02-25
1    2 2021-03-02
2    3 2021-02-23
3    4        NaT
"""

#to remove the date in a row with empty
wrgdata.dropna(subset=['date'],inplace=True)
print(wrgdata.to_string())
"""
   sno       date
0    1 2021-02-25
1    2 2021-03-02
2    3 2021-02-23
"""

#to add the values in csv in specific rows
wrgdata.loc[4,"date"]="25/09/21"
wrgdata.loc[4,"sno"]="NaN"
print(wrgdata.to_string())
"""
   sno                 date
0  1.0  2021-02-25 00:00:00
1  2.0  2021-03-02 00:00:00
2  3.0  2021-02-23 00:00:00
4  NaN             25/09/21
"""

#to change the data in big data
for x in wrgdata.index:
    if wrgdata.loc[x, "sno"] == "NaN":
        wrgdata.loc[x, "sno"] = x+1

print(wrgdata.to_string())
