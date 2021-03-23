greet={"welcome","to","python"}

print("welcome" in greet)
#true

#cannot modify existing values in the set
#but can add new items to the set

#to add new items to greet set
greet.add("programming")
print(greet)
#{'python', 'programming', 'to', 'welcome'}

#use update to add items from another set,list,tuple to this set
set2={"is","very","popular"}
greet.update(set2)
print(greet)