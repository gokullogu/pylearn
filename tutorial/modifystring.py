a="Hello World"
print(a.upper())#HELLO WORLD

print(a.lower())#hello world

whitespace=" hello world "
print(whitespace.strip()) 

replace_txt="Hello world"
print(replace_txt.replace("H","F"))

#string to tuple 
str_split="hello world hai hello welcome you all"
print(str_split.split(" "))

#str concat using +
str_con1="good"
str_con2="morning"
print(str_con1 +" "+str_con2)

#combining str and num is error
age_conc=19
#str_cont="my name is john "+age_conc
#print(str_cont)

#to concat str and num
age_conct=19
str_conct="My name is john and I am {}"
print(str_conct.format(age_conct))

#format can take any num of arguments
dd=25
mm=3
yyyy=2002
print("my dob is {}/{}/{}".format(dd,mm,yyyy)) 
#or
print("my dob is {2}/{1}/{0}".format(dd,mm,yyyy))

#double qouates in double quotes is error
#doblqot="welocome you all "here""
#print(doblqot)

doblqot = "welocome you all \"here\""
print(doblqot)






 



