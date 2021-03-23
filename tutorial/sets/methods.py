#methods for set

#add
addset={"good","bad","worst"}
print(addset.add("bad"))
#none      
# because duplicate value


#clear empties the entire set
addset.clear()
print(addset)
#set()

#discard removes an item if exists but will not cause any error if not exist
discardset={"apple","eat","good","for"}
discardset.discard("for")
print(discardset)
#{'good', 'eat', 'apple'}

#or

#remove deletes the value specified
removeset={"remove","set","removes","specified","value"}
removeset.remove("set")
print(removeset)
#'removes', 'remove', 'value', 'specified'}

#copy the set to new set
cset={"use","copy","to","copy","an","set","to","another","set"}
copyset=cset.copy()
print(copyset)
#{'another', 'use', 'to', 'an', 'copy', 'set'}

#difference
set1={1,2,3,4}
set2={2,4,6}
set3=set1.difference(set2)
print(set3)
#{1,3}

#difference_update
set1 = {1, 2, 3, 4}
set2 = {2, 4, 6}
set1.difference_update(set2)
print(set1)
#{1,3}

#isdisjoint returns true if intersection of set1 and set2 is 0
set1 = {1, 2, 3, 4}
set2 = {2, 4, 6}
set3=set1.isdisjoint(set2)
print(set3)
#false

#issubset returns if set1 contains all set2 values
set1 = {1, 2, 3, 4}
set2 = {2, 4}
set3 = set2.issubset(set1)
print(set3)
#true

#issuperset returns true if all items in set2 are in set1
set1 = {1, 2, 3, 4}
set2 = {2, 4}
set3 = set1.issuperset(set2)
print(set3)
#true

#pop removes an random value in list
set1 = {1, 2, 3, 4}
a=set1.pop()
print(a)
#1









