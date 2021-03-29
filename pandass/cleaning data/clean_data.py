import pandas as pd

#empty rows can give us a wrong result

dirt=pd.read_csv('pandass/cleaning data/dirtydata.csv')

#to remove empty rows use dropna 
#dropna creates new instance of csv as new_dirt
#changes in new_dirt will not get affect the dirt
new_dirt=dirt.dropna()

#use inplace=true in case if you want to delete empty rows in the original csv want to be changed 
#dirt.dropna(inplace=True)

print(new_dirt.to_string())
#   Duration          Date  Pulse  Maxpulse  Calories
#0        60  '2020/12/01'  110.0       130     409.1
#2        60  '2020/12/03'  103.0       135     340.0
#4        45  '2020/12/05'  117.0       148     406.0

#use fillna to replace nan by values
#dirt.fillna(0,inplace=True)
print(dirt.to_string())
#   Duration          Date  Pulse  Maxpulse  Calories
#0        60  '2020/12/02'    0.0       117     479.0
#1        60  '2020/12/02'    0.0       117     479.0
#2        60  '2020/12/03'  103.0       135     340.0
#3        45             0  109.0       175     282.4
#4        45  '2020/12/05'  117.0       148     406.0
#5        23   '2020/2/23'  123.0       324       0.0

#to replace empty rows for only one column use column name
dirt["Date"].fillna("yyyy/mm/dd",inplace=True)
print(dirt.to_string())
#Duration          Date  Pulse  Maxpulse  Calories
#0        60  '2020/12/01'  110.0       130     409.1
#1        60  '2020/12/02'    NaN       117     479.0
#2        60  '2020/12/03'  103.0       135     340.0
#3        45    yyyy/mm/dd  109.0       175     282.4
#4        45  '2020/12/05'  117.0       148     406.0
#5        23   '2020/2/23'  123.0       324       NaN


