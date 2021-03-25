dictpop={
    "name":"L",
    "name":"gokul",
    "age":19,
    "place":"pollachi"
}


#to delete the key "name " use pop()
dictpop.pop("name")
print(dictpop)
#{'age': 19, 'place': 'pollachi'}

#to delete the last item in dictionary use popitem()
dictpop.popitem()
print(dictpop)
#{'age': 19}

#empties the dictionary leaving the dict 
dictpop.clear()
print(dictpop)
#{}

#deletes the dictionary completely 
del dictpop
print(dictpop)

