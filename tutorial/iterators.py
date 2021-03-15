nutrients=("calcium","protein","vitamin D")
myit=iter(nutrients)

print(next(myit))
print(next(myit))
print(next(myit))

#to create class object as an iterator
class mynum:
    #to initialize iterator user iter func
    def __iter__(self):
        self.a=1
        return self
    #to iterate the value use nec=xt func
    def __next__(self):
        x=self.a
        self.a+=1
        return x

mn1=mynum()
myiter=iter(mn1)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#to print a iter in short code


class mynumloop:
    #to initialize iterator user iter func
    def __iter__(self):
        self.a = 1
        return self
    #to iterate the value use nec=xt func

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

mn2=mynumloop()
myiter2=iter(mn2)

for x in myiter2:
    print(x)