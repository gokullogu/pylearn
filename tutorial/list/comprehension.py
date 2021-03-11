fruits=["apple","banana","jackfruit","pineapple"]

#prints the list item containing "n" in it
new=[]
for i in fruits:
    if "n" in i:
        new.append(i)
print(new)    
#['banana', 'pineapple']

#using comprehension do this shorter
new2=[x for x in fruits if "n" in x]
print(new2)
#['banana', 'pineapple']

#create an list from 0 to 9
printuptoten=[x for x in range(10)]
print(printuptoten)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#to create with condition >5
printlessthan=[x for x in range(10) if x>5]
print(printlessthan)
#[6, 7, 8, 9]

#to print value orange when value is banana
wobanana=[x if x!="banana" else "mango" for x in fruits]
print(wobanana)
#['apple', 'mango', 'jackfruit', 'pineapple']

