#while loop
print("while")
i=1
while i<=10:
    print(i)
    i+=1

#continue 
print("continue")
i=0
while i<6:
    i=i+1
    if i==3:
        continue
    print(i)

#while with else
print("while with else")
i=0
while i<6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")    