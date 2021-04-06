n=int(input())
m=int(input())
nlist=[]
mlist=[]
mislist=[]
print("list 1")
for i in range(n):
    inp=int(input())
    nlist.append(inp)

print('list2')
for i in range(m):
    inp = int(input())
    mlist.append(inp)

def issame(nlist,mlist):
    print("missing elements are")
    for i in range(len(mlist)):
        if (mlist.count(mlist[i])>1):
            if(mlist.count(mlist[i]!=nlist.count(nlist[i])):
                if(mlist[i] not in mislist):
                    mislist.append(mlist[i])
    
    
issame(nlist,mlist)
