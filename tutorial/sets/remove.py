delset={"items","in","set","are","unordered"}
delset.remove("in") #removes the in from delset
print(delset)
#{'are', 'items', 'set', 'unordered'}

#use discard() if no error should be thrown if item not present
delset.discard("program") #will not get error
print(delset)
#{'unordered', 'items', 'are', 'set'}

#use clear the set only values
delset.clear()
print(delset)
#set()

#use del to entirely delete the set
del delset
print(delset)

