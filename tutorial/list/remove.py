#remove() removes item sepecified
fruit=["mango","orange","papaya"]
fruit.remove("mango")
print(fruit)
#['orange', 'papaya']

#pop() removes the list item at specified index
this_list=["john","19","poland"]
this_list.pop(1)
print(this_list)
#['john', 'poland']

#pop() removes the last item if  unspecified 
this_list1 = ["john", "19", "poland"]
this_list1.pop()
print(this_list1)
#['john', '19']

#del without index deletes the list completely 
thislist2=["xenon","randon","zinc"]
del thislist2
#print(thislist2)
#NameError: name 'thislist2' is not defined

#del woth index delete the item at specified index
chem=["H2O","H2","OH"]
del chem[0]
print(chem)
#['H2', 'OH']

#clear method empties the list but do not delete it
lan=["c","cpp","java","python"]
lan.clear()
print(lan)