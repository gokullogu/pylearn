#nested dect
#three dict inside one dict
car={
    "car1":{
       "brand":"suzuki",
       "model":"shift"
    },
    "car2":{
      "brand":"honda",
      "model":"amaze" 
    },
    "car3":{
     "brand":"ford",
     "model":"eco-sports"
    }
}
print(car)
#{'car1': {'brand': 'suzuki', 'model': 'shift'}, 'car2': {'brand': 'honda', 'model': 'amaze'}, 'car3': {'brand': 'ford', 'model': 'eco-sports'}}

#or
bike1 = {
    "brand": "royal enfield",
    "model": "classic"
},
bike2 = {
    "brand": "star city",
    "model": 110
}
bikedet={
  "bike1":bike1,
  "bike2":bike2
}
print(bikedet)
