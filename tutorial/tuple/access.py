
cars=("bmw","rolls royce","MG hector","tata tigor","audi","creta")
print(cars)
#('bmw', 'rolls royce', 'MG hector', 'tata tigor', 'audi', 'creta')

#second item
print(cars[1])
#rolls royce

#last item index -1
print(cars[-1])
#creta

print(cars[2:4])
#('MG hector', 'tata tigor')

print(cars[-5:-1])
#('rolls royce', 'MG hector', 'tata tigor', 'audi')

print(cars[-5:])
#('rolls royce', 'MG hector', 'tata tigor', 'audi', 'creta')

print(cars[4:5])

if "creta" in cars:
    print("creta is in the tuple")

#we cannot directly add tuples
#they are immutable or unchangable
biketuple=("duke","shine","yamaha","apache")
print("\n","before change :",biketuple)
bikelist=list(biketuple)
bikelist[2]="fascino"
biketuple=tuple(bikelist)
print("after change :",biketuple)

#to delete item from tuple
mobiletuple=("lava","redmi","mi","samsung")
mobilelist=list(mobiletuple)
mobilelist.remove("lava")
mobiletuple=tuple(mobilelist)
print(mobiletuple)

#to delete the tuple
deltuple=("item1","item2","item3")
print(deltuple)
del deltuple
#print(deltuple)
