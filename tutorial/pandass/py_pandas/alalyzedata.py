import pandas as pd

dread=pd.read_csv('pandass/py_pandas/data.csv')

#head() selects first five rows
print(dread.head())

#tail() selects last five rows from the last row
print(dread.tail())

#info method of dataframe gives more information
print(dread.info())

print(dread.to_string())
