set1={"a","b","c"}
set2={1,2,3}

#use union to merge two sets
set3=set1.union(set2)
print(set3)
#{'b', 'c', 1, 2, 3, 'a'}
#or 
#use update()
set1.update(set2)
print(set1)
#{'b', 'c', 1, 2, 3, 'a'}

#to keep only duplicates
set4={"microsoft","apple","zoho"}
set5={"zoho","apple","samsung"}
set4.intersection_update(set5)
print(set4)
#{'zoho', 'apple'}

#return new set with values present on both set
set4 = {"microsoft", "apple", "zoho"}
set5 = {"zoho", "apple", "samsung"}
set6=set4.intersection(set5)
print(set6)    
#{'zoho', 'apple'}

#keeps values that are not present in both sets
set4 = {"microsoft", "apple", "zoho"}
set5 = {"zoho", "apple", "samsung"}
set4.symmetric_difference_update(set5)
print(set4)
#{'microsoft', 'samsung'}

#or
set4 = {"microsoft", "apple", "zoho"}
set5 = {"zoho", "apple", "samsung"}
set6=set4.symmetric_difference(set5)
print(set6)
#{'microsoft', 'samsung'}





#union=intersection=symmetric_difference
#--creates new set

#update=intersection_update=symmetric_difference_update
#--updates the existing set




