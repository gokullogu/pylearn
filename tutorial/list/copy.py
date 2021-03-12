lis1=["orange","grapes","fig"]
lis2=lis1
lis2[0]="apple"
print(lis2)
print(lis1)
#but changes in lis2 will chane lis1 also

#use copy method to do it
listorg=["gokul","john","ram"]
listcpy=listorg.copy()
print(listcpy)
#['gokul', 'john', 'ram']

#or use list an built in method to copy
listorg1=["car","bus","helicopter"]
listorg2=list(listorg1)
print(listorg2)
#['car', 'bus', 'helicopter']
