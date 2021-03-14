#module is  an code library
# consists of code
import greet
greet.greeting("gokul L")

print(greet.per1["age"])

#use "as" to give the alias name of module
import rename as name
name.name("goku")

#built in modules
import platform
sysname=platform.system()
print(sysname)

#prints all the functions  in platform
print(dir(platform))

#module consists of several object 
#to import only one obj but not all use from and import

from greet import greeting
greeting("raj")