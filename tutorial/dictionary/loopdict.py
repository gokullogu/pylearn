dict={
    "name":"gokul",
    "age":19,
    "dob":"25/03/2002",
    "place":"pollachi",
    "roll no":"19BIT077"
}

#returns all the keys of the dict 
for x in dict:
    print(x)
#name
#age
#dob
#place
#roll no

#use values prints all the values in dictionary
for x in dict.values():
    print(x)
#gokul
#19
#25/03/2002
#pollachi
#19BIT077

#or
for x in dict:
    print(dict[x])
#gokul
#19
#25/03/2002
#pollachi
#19BIT077

#to print all the keys in the dict
for x in dict.keys():
    print(x)
#name
#age
#dob
#place
#roll no

#to print the items i.e (key,values) tuple in list
for x,y in dict.items():
    print(x,y)
#name gokul
#age 19
#dob 25/03/2002
#place pollachi
#roll no 19BIT077


