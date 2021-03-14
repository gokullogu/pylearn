#local scope
def myloc():
    x=30
    print(x)
myloc()
#print(x) will throw error because x is local

#both print(z) will be printed
z=90
def myglob():
    print(z)

myglob()
print(z)

#to use the function from outside function use global before object name

def glob():
    global a
    a = 321
glob()
print(a)

    


