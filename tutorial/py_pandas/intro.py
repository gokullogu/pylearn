import pandas as pd

#to know the version
print(pd.__version__,"\n")
#1.2.3


#dict
mydataset={
    'cars':["bmw","volvo","ford"],
    'passings':[3,7,2]
}
pdvar=pd.DataFrame(mydataset)
print(pdvar,"\n")

#simple pandas series
print(" ","pandas series")
a=[3,4,2,6]
pdser=pd.Series(a)
print(pdser,"\n")

#simple pandas series with index x,y,z
print("pandas series with alphabet index")
a = [3, 4, 2, 6]
pdser = pd.Series(a,index=["w","x","y","z"])
print(pdser,"\n")

#to select specific data
print("specific details in dict")
mydet={
    "name":"gokul",
    "age":19,
    "rollno":"19BIT077"
}
mydetvar=pd.Series(mydet,index=["name","rollno"])
print(mydetvar,"\n")


