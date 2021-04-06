list=[]
left=[]
n=int(input("enter the length:"))
print("enter",n,"values")
for i in range(n):
    val=int(input())
    if(val==i):
        list.append(val)

for i in range(0,n):
        left.append(i)
print("left elements:",left)
