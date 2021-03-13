#creating functions
def my_fun():
    print("hello world")
my_fun()
#hello world

#function with argument
def namefun(fname,lname):
    print(fname+" "+lname)
namefun("gokul","L")
#gokul L

#namefun("gokul") will cause to error


#using argument tuple to get values
def namefun(*name):
    print(name[2])
namefun("emil","john","britto")
#britto

#using keyword arguments child1,2,3
#if keyword arguments number known
#changing order will not change the value
def kname(child3,child1,child2):
    print(child3)
kname(child1="emil",child2="tobias",child3="john")
#emil

#if number of keyword  unknown
#uses dict of arguments
def kwname(**kid):
    print("name is "+kid["fname"])
kwname(fname="tharun",lname="balaji")

#default parameter value
def country(countryname="India",state="Tamil Nadu"):
    print("I am from ",state,",",countryname,".")
country("srilanka","kandy")
country()

#passing list as list
fruits=["apple","mango","pineapple"]

def my_fru(fruits):
    for x in fruits:
        print(x)
my_fru(fruits)

#function returns a statement
def my_ret(x):
 return 5*x
print(my_ret(3))   

#recursive function to print sum of 0 to 5
def rec_fun(k):
    if(k>0):
        x=k+rec_fun(k-1)
        print(x)
    else:
        x=0
    return x
    
rec_fun(5)