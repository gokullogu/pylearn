#regxp
#to find the string match of pattern

import re

txt="The rain in the mountain"

x=re.search("^The rain",txt)
#^to start the matching when "The"
#$to end the matching when "rain"
#* more occurences

if x:
    print("pattern matched")
else:
    print("not found")

#prints the matched letters between a and m
print(re.findall("[a-z]","India"))

#find all digit characters
print(re.findall("\d","there are 365 days in 1 year"))

#searches for h...o in with hello
print(re.findall("h...o","hello"))

#one or more occurences
print(re.findall("gokul+","hello gokul welcome gokul"))

#zero or more occurences
print(re.findall("^gokul*","gokul in pollachi gokul"))

#more occurences
print(re.findall("^gokul{2}", "gokul in pollachi gokul"))

#or
print(re.findall("falls|stays","spain falls in the plain"))

#special characters
print(re.findall("\AThe","The legend"))