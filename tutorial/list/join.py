
list1=["a","b","c"]
list2=["e","d","f"]

#use + to join two strings
print(list1+list2)
#['a', 'b', 'c', 'e', 'd', 'f']

#or adding one by one item from list2 to list1
for x in list2:
    list1.append(x)
print(list1)    
#['a', 'b', 'c', 'e', 'd', 'f']

#use also extend to join list1 to list2
list2.extend(list1)
print(list2)
#['e', 'd', 'f', 'a', 'b', 'c', 'e', 'd', 'f']

app1=["app",1,"is","append","list",1]
app2 = ["app", 2, "is", "append", "list", 2]
app1.append(app2)
print(app1)


