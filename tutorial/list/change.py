clist=["lava","apple","mi","sony","samsung","oneplus"]

#to replace list at pos 0
clist[0]="rog"
print(clist)
#['rog', 'apple', 'mi', 'sony', 'samsung', 'oneplus']

clist[2:4]=["realme","redmi"]
print(clist)
#['rog', 'apple', 'realme', 'redmi', 'samsung', 'oneplus']

clist[2:4] = ["realme", "redmi","rog3"]
print(clist)
#['rog', 'apple', 'realme', 'redmi', 'rog3','samsung', 'oneplus']

clist[2:6]=["r's"]
print(clist)
#['rog', 'apple', "r's", 'oneplus']

#insert value at specified index
clist.insert(2,"maxx")
print(clist)
#['rog', 'apple', 'maxx', "r's", 'oneplus']


