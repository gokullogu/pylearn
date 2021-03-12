a=90
#if statement
if a==90:
 print("a is equal to ninety")
#a is equal to ninety

#elif to execute if previous is false
num1=25
num2=34
if num2<num1:
    print("num1 is greater")
elif num1<num2:
    print("num2 is greater")   
#num2 is greater

#else to execute statement
# if ,elif condition fails
num3=56
num4=56
if num3>num4:
    print("num3 is greater")
elif num3<num4:
    print("num4 is greater")
else:
    print("both num3 and num4 are equal")
#both num3 and num4 are equal

#short hand if    
num5=90
num6=90
if num5==num6: print("num5 is equal to num6")
#num5 is equal to num6

#short hand ifelse
num7=56
num8=66
print("num7 is greater") if num7>num8 else print("num8 is greater")
#num8 is greater

#one line with three conditions
terta=12
tertb=13
print("A") if terta>tertb else print("B") if terta<tertb else print("equal")

#and
a1=34
b1=23
if a1<50 and b1<50:
    print("hello")

#use pass if 'if' is empty
a4=90
b4=123
if b4>a4:
    pass

