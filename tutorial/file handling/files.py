#file handling is an important part of any web app

f=open("demo.txt","r")
print(f.read()," ")
f.close()
#Programming in python
#Python is most popular programming language
#Python is very easy to learn
#Python has large scope.

#returns the number of characters specified
f1=open("demo.txt","r")
print(f1.read(5)," ")
f1.close()
#Progr

#return one line using readline() 
#call readline twice to print first two line
f2=open("demo.txt","r")
print(f2.readline())
print(f2.readline())
f2.close()
#Programming in python

#Python is most popular programming language


#loop through text file line by line
f3=open("demo.txt","r")
for x in f3:
    print(x)

#Programming in python

#Python is most popular programming language

#Python is very easy to learn

#Python has large scope.


#to close the file 
f3.close()
