#class is an object constructor or blue print for class
class Myclass:
    x=25
#creating objects
p1=Myclass()
print(p1.x)

#class with init function
#init is default function of any class 
#to assign value to object properties
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=person("gokul",18)
print(p1.name)
print(p1.age)

#create an method in class object 
class Details:
    def __init__(self,name,place):
        self.name=name
        self.place=place
    
    def myfunc(self):
        print("I am ",self.name," from ",self.place)

det1=Details("gokul","pollachi")
det1.myfunc()

#self can be replaced by any word
#but it must be first argument of any function in class


#modify the properties value by objname.prop
det1.name="krish"
print(det1.name)

#to del property of object
del det1.place
#print(det1.place) will throw an error

#to create an empty class use pass
class empty:
    pass
