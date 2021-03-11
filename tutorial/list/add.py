#to add the the value to end of list use append
cars=["audi","bens","rolls royce"]
cars.append("bmw")
print(cars)
#['audi', 'bens', 'rolls royce', 'bmw']

#to append the list to the list use extend
fruit=["apple","mango","banana"]
veg=["carrot","beetroot","brinjal"]
fruit.extend(veg)
print(fruit)
#['apple', 'mango', 'banana', 'carrot', 'beetroot', 'brinjal']

#to append the set,tuples,dictionaries to list use extend
name=["john", "peter", "kenn"]
details=(18, "america")
name.extend(details)
print(name)
#['john', 'peter', 'kenn', 18, 'america']
