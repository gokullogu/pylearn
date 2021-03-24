import pandas as pd
#dataframe is an multi dimentional table
#dataframe to display student details
stud = {
    "name": ["gokul", "ram", "tharun"],
    "age": [18, 19, 19],
    "class": ["IT-A", "IT-A", "IT-A"],
    "place": ["pollachi", "udumalaipet", "madurai"]
}
studvar = pd.DataFrame(stud)
print(studvar)

#loc to select row by its index
for i in range(len(studvar)):
    print(studvar.loc[i])
