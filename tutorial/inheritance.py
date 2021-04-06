#parent class is base from which other class inheris
#derived class derived from base

#base class
class Parent:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    def printname(self):
        print("I am ",self.fname,"",self.lname)

par1=Parent("ram","prakash")
par1.printname()
        
#derived class
#pass base as derived class argument
class Studentcls1(Parent):
    pass

#creating object for derived class
std1=Studentcls1("gokul","L")
std1.printname()

#student class inherits the methods and properties
#from base class

#when __init__() is added to student 
#will no longer inherit from base class

class Studentcls2(Parent):
    def __init__(self,fname,lname):
        self.lname=lname
        self.fname=fname
    
    def printname(self):
        print("I am","",self.lname,"",self.fname)


#creatind object for student after creating an init for student
std1=Studentcls2("tharun","balaji")
#only printname in student will work ,but not inherit parent's class printname
std1.printname()


#to inherit parent's init to student init 
#add parent.init func inside the student's init func
class Studentcls3(Parent):
    def __init__(self,fname,lname):
        Parent.__init__(self,fname,lname)

    def printname(self):
        print(self.fname,"is printed from derived class")

std1=Studentcls3("dhanush","J")
std1.printname()


#the same using super function
#adding self to super init will cause error
class Studentspr(Parent):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
    
    def printname(self):
        print(self.fname)

std1=Studentspr("John","D")
std1.printname()

#to add parameter
class Studentcls4(Parent):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.year=year
std1=Studentcls4("hari","H",2021)
std1.printname()
print(std1.year)

#add method to student class
class Studentcls5(Parent):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

    def welcome(self):
        print("welcome","",self.fname,"",self.lname)

std1=Studentcls5("raja","L")
std1.welcome()
