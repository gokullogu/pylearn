#values in dictionary can be accessed by
#  key name inside brackets

dictacc = {
    "brand": "ford",
    "model": "mustang",
    "year": "1990"
}
x = dictacc["year"]
print(x)
#1990

#or
#use get("key name")
x = dictacc.get("model")
print(x)
#mustang


#keys() method returns the list of all keys in dict
x = dictacc.keys()
print(x)
#dict_keys(['brand', 'model', 'year'])

#adding new key in dictionary will affect the method keys
dictacc["warrenty"] = "2 years"
print(x)
#dict_keys(['brand', 'model', 'year', 'warrenty'])

#values() method returns the list of all values  of dict
x = dictacc.values()
print(x)
#dict_values(['ford', 'mustang', '1990', '2 years'])

#changes in values in dictionary will affect the values method
dictacc["year"] = 2021
print(x)
#dict_values(['ford', 'mustang', 2021, '2 years'])

#items will returns the each value key pairs as tuples
# all tuples inside one list
x = dictacc.items()
print(x)
#dict_items([('brand', 'ford'), ('model', 'mustang'), ('year', 2021), ('warrenty', '2 years')])

#changing the value in dictionary items() get affected
dictacc["model"] = "maruthi"
print(x)
#dict_items([('brand', 'ford'), ('model', 'maruthi'), ('year', 2021), ('warrenty', '2 years')])

#adding new key,value pair to dictionary gets affected in items
dictacc["date"] = "25/4/20"
print(x)
#dict_items([('brand', 'ford'), ('model', 'maruthi'), ('year', 2021), ('warrenty', '2 years'), ('date', '25/4/20')])

#if key exists in dictionary returns print
if "model" in dictacc:
    print("model is in dictionary dictacc")
