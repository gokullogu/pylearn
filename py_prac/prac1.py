"""a=int(input("enter num 1:"))
b=int(input("enter the num 2:"))
for x in range(a,b):
    if x%7==0 and x%5==0:
        print(x)

for word in ('hello','welcome','all'):
    print(str(word))"""

"""x=5
while x>0:
    print(x*"*")
    x-=1

x=5
y=x==6
z=x==5
print(y)
print(z)


def days_in_years(year):
    if (year==1):
        print("1 year has 365 days")
    else:
        print("number of days in",year,"years","are",year*365)

days_in_years(int(input("enter the number of years:\n")))

def to_celcius(deg_feh):
    deg_cel=(deg_feh-32)*5/9
    return deg_cel

print(to_celcius(32.0))


def calculate_carton(num_eggs):
    num_carton=num_eggs/12
    return num_carton

print("number of cartons required")

def maxmin(list):
    list.sort()
    print(list[0])
    print(list[4])
    
print("enter the 5 integers:")

list=[]
for x in range(5):
    list.append(input())
    maxmin(list)"""

class str:
    def __init__(self,inp_str):
        self.inp_str=inp_str

    def print_string(self):
        strupp=self.inp_str
        print(strupp.upper())

str1=str("hello world")
str1.print_string()

def x_at_either_end(str):
    #for i in str:
        if(str[0]=='x') or (str[-1]=='x'):
            return True
        else:
            return False

print(x_at_either_end("hello worldx"))




        
        
        

