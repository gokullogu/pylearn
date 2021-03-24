#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered and unindexed. No duplicate members.
#Dictionary is a collection which is unordered and changeable. No duplicate members.


#dict are ordered changable non duplicated key:value pairs
dict1={
    "name":"gokul",
    "year":2002
}

print(dict1)
#{'name': 'gokul', 'year': 2002}

print(dict1["year"])
#2002

#duplicate values will override existing values
dupdict={
    "name":"harry",
    "place":"switzerland",
    "place":"india"
}
print(dupdict)
#{'name': 'harry', 'place': 'india'}

#len returns the number of key value pairs in a dict
print(len(dict1))
#2

#type returns dict
print(type(dict1))
#<class 'dict' >

#dict key's value can be of any datatype
car1={
    "brand":"volvo",
    "auto-gear":True,
    "year":2019,
    "color":["red","blue","yellow"]   
}
print(car1)
