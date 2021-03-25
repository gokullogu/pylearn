lan={
    "name":"python",
"oop":True
}

#setdefault() sets the value of key if key does not exist
lan.setdefault("oop",False)

#returns the list of tuple of values
print(lan.values())
#dict_values(['python', True])

#fromkeys convertst the iterable to dictionary
x=('key1','key2','key3')
y=8
dicx=dict.fromkeys(x,y)
print(dicx)
#{'key1': 8, 'key2': 8, 'key3': 8}


