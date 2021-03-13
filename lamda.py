#lamda function contains 
#n number of args but only one expression
x=lambda a,b:a+b
print(x(1,2))
#3

#doubles the value when lamda is inside a function

def mydoub(n):
    return lambda a:a*n

mydoubler=mydoub(2)

print(mydoubler(12))

#triples the number
def mytrip(n):
    return lambda a:a*n
mytripler=mytrip(3)

print(mytripler(123))