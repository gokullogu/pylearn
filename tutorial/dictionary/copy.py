#use copy() to copy from one dict to another
bike={
    "brand":"honda",
    "model":"shine",
    "year":2019,
    "warrenty":2
}

#to copy the dict using copy()
bike1=bike.copy()
print(bike1)
#{'brand': 'honda', 'model': 'shine', 'year': 2019, 'warrenty': 2}

#or
bike2=dict(bike)
print(bike2)
#{'brand': 'honda', 'model': 'shine', 'year': 2019, 'warrenty': 2}

