import pandas as pd

#empty rows can give us a wrong result

dirt=pd.read_csv('cleaning data/dirtydata.csv')

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


#insteading odf using the same value to all cells
#use mean(),median() and mode() to add the values to the empty cell


#mean = sum of all values /total number of values
mdirdt=pd.read_csv('cleaning data/dirtydata.csv')
x=mdirdt["Maxpulse"].mean()
mdirdt["Maxpulse"].fillna(x,inplace=True)
print(mdirdt.to_string())
"""
   Duration          Date  Pulse  Maxpulse  Calories
0       NaN  '2020/12/01'  110.0     130.0     409.1
1      60.0  '2020/12/02'    NaN     117.0     479.0
2       NaN  '2020/12/03'  103.0     178.8     422.0
3      45.0           NaN  109.0     175.0     282.4
4       NaN  '2020/12/05'  117.0     148.0     406.0
5      23.0   '2020/2/23'  123.0     324.0       NaN
"""


#mean = middle value in the column in ascending
meddirt=pd.read_csv('cleaning data/dirtydata.csv')
x = meddirt["Duration"].median()
mdirdt["Duration"].fillna(x,inplace=True)
print(meddirt.to_string())
"""
   Duration          Date  Pulse  Maxpulse  Calories
0       NaN  '2020/12/01'  110.0     130.0     409.1
1      60.0  '2020/12/02'    NaN     117.0     479.0
2       NaN  '2020/12/03'  103.0       NaN     422.0
3      45.0           NaN  109.0     175.0     282.4
4       NaN  '2020/12/05'  117.0     148.0     406.0
5      23.0   '2020/2/23'  123.0     324.0       NaN
"""

#mode = selects the frequent value in the column if no values are frequent takes the least value
modedirt = pd.read_csv('cleaning data/dirtydata.csv')
x = modedirt["Calories"].mode()[0]
modedirt["Calories"].fillna(x, inplace=True)
print(modedirt.to_string())
"""
   Duration          Date  Pulse  Maxpulse  Calories
0       NaN  '2020/12/01'  110.0     130.0     409.1
1      60.0  '2020/12/02'    NaN     117.0     479.0
2       NaN  '2020/12/03'  103.0       NaN     422.0
3      45.0           NaN  109.0     175.0     282.4
4       NaN  '2020/12/05'  117.0     148.0     406.0
5      23.0   '2020/2/23'  123.0     324.0     282.4
"""
