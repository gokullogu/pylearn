fruits=("apple","grapes","banana")
(green,blue,red)=fruits

#unpacking tuple is assigning the values from tuple to variables
print(green)
#apple
print(blue)
#grapes
print(red)
#banana

#if number of variables less than number of list values use * asterisk to last
obj=("teddy","house","pen","bike")

(value1,*values)=obj

print(value1)
#teddy
print(values)
#['house', 'pen', 'bike']
print("")

#when asterisk used with the second last variable
(val1,*val2,vals)=obj  

print(val1)
#teddy       first value to variable 1
print(val2)
#['house', 'pen']   remaining values except last value to variable 2 
print(vals)
#bike      last value to last variable






