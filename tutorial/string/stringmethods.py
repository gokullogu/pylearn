#capitalize()
# first letter of every obj
print("hello google".capitalize())
# Hello google

#if number is first results the same number


#casefold() 
# is same as lower() but efficient
print("Welcome To Python".casefold())
#welcome to python

#center()
#prints str after 20 characters
print("banana".center(20)) 
#       banana

#count()
#count number of instances of str in str
print("welcome world hello world".count("world"))
#2


#encode()
#encode the given string defaultly to utf8
strdecp = "hello pythön is the secret password"
strencp=strdecp.encode();
print(strencp)
#b'hello pyth\xc3\xb6n is the secret password'

#endswith()
#returns true if match is found at end
print("Hello world !".endswith("!"))
#true

#or 
# string.endswith("pattern",search start,search end)
print("hello world is the common word.".endswith("word.",1))
#true

#expandrtabs()
# sets \t to specied size

#default
print("h\te\tl\tl\to")
#h       e       l       l       o

print("size 2 :h\te\tl\tl\to".expandtabs(2))
#size 2: h e l l o

print("size 3 :h\te\tl\tl\to".expandtabs(3))
#size 3 :h   e  l  l  o

#format()
#format to
#empty index
print("I am {} and I am {}".format("tharun",19))
#I am tharun and I am 19

#numbered index
print("I am {} and I am {}".format("raja",19))
#I am raja and I am 19

#named index
print("I am {name} and {age}".format(name="gokul",age="19"))
#I am gokul and I am 19



#format types
#thousand seperator
print("The universe is {:,} years old".format(123456789))
#The universe is 123, 456, 789 years old

#to add values to placeholder with sign +,-
print("The temperatue is between {:+} and {:+}".format(-10,5))
#The temperatue is between - 10 and +5

#use minus for negative values only
print("The temperatue is between {:-} and {:-}".format(-10, 5))
#The temperatue is between - 10 and 5

#to add space before value 
print("The temperatue is {:<8} celcius".format(15))
#The temperatue is 15       celcius

#to add space after value
print("The temperatue is {:>8} celcius".format(15))
#The temperatue is       15 celcius

#to add space before and after value
print("The temperatue is {:^8} celcius".format(15))
#The temperatue is    15    celcius

#number to binary
print("binary value of {0} is {0:b}".format(5))

print("decimal value of {:d} is ")