#sort the str list in asc order
ascstrlist = ["everest","aeroplane","bike","car","driver"]
ascstrlist.sort()
print(ascstrlist)
#['aeroplane', 'bike', 'car', 'driver', 'everest']

#sort the num list in asc
ascnumlist=[34,12,89,33,48]
ascnumlist.sort()
print(ascnumlist)
#[12, 33, 34, 48, 89]

#sort the str list in dsc order
dscstrlist = ["everest", "aeroplane", "bike", "car", "driver"]
dscstrlist.sort(reverse=True)
print(dscstrlist)
#['everest', 'driver', 'car', 'bike', 'aeroplane']

#sort the num list in dsc
dscnumlist = [34, 12, 89, 33, 48]
dscnumlist.sort(reverse=True)
print(dscnumlist)
#[89, 48, 34, 33, 12]

#sort the list based on return of results in ascending order from function
def myfun(n):
    return abs(n-50)
numfun=[100,37,12,90,12]
numfun.sort(key=myfun)
print(numfun)
#[37, 12, 12, 90, 100]

#sort gives wrong answer as sorting is not in alphabetical order
errlist=["apple","Mango","Banana","papaya"]
errlist.sort()
print(errlist)
#['Banana', 'Mango', 'apple', 'papaya']

#to solve this sort by using predefined function str.lower
errlist.sort(key=str.lower)
print(errlist)
#['apple', 'Banana', 'Mango', 'papaya']

#reverses the list sinply without sorting it
errlist.reverse()
print(errlist)
#['papaya', 'Mango', 'Banana', 'apple']


