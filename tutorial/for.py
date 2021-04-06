#for inside list
name=["vishnu","ram","gopal","vignesh"]
for i in name:
    print(i)

#loop through a string
print("\n","looping string")
for x in "john lee":
    print(x)


#break loop when name is gopal
print("\n","break")
for x in name:
    print(x)
    if x=="gopal":
        break;

#continue skips when gopal
print("\n","continue")
for x in name:
    print(x)
    if x=="ram":
        continue
#vishnu
#ram
#gopal
#vignesh

#range to iterate code several times
for x in range(6):
    print(x)

#range from 2 to 6
print("\n","range from 2 to 6")
for x in range(2,6):
    print(x)
# range from 2 to 6
#2
#3
#4
#5

#to increment by 3
print("\n","to print multiple of 3")
for x in range(3,30,3):
    print(x)
# to print multiple of 3
#3
#6
#9
#12
#15
#18
#21
#24
#27

#print upto 6
print("\n","print upto 6")
for x in range(6):
    print(x)
else:
    print("x not less than 6")   
# print upto 6
#0
#1
#2
#3
#4
#5
#x not less than 6
    

#if for is empty
for x in [0,1,2]:
    pass

#nested loop
print("\n","nested for loop")
adj=["red","big","tasty"]
fruits=["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)
# nested for loop
#red apple
#red banana
#red cherry
#big apple
#big banana
#big cherry
#tasty apple
#tasty banana
#tasty cherry

#for with break
print("\n","for with break")
for x in range(6):
    if x==3:
        break
    print(x)
else:
    print("finished for loop")
# for with break
#0
#1
#2

