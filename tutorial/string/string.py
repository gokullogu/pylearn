print("hello all")

print("gokul L")

a="gokul"
print(a)

"""multi line string"""
multstr="""lorem ipsum ipsum lorem ipsum"""
print(multstr)

"""string is a array "h" is a string"""
strlen="hello world"
print(strlen[1])

"""looping"""
for x in "gokul":
    print(x)

"""length of a string"""
strlen2="gokul logu"
print(len(a))

"""true if string pattern is found"""
print("logu" in strlen2)

txt="best things in life are free"
if "life" in txt:
    print("yes ,free is there")

"""true if not present"""
print("bet" not in txt)

if "bet" not in txt:
    print("no ,bet is not there")

strslice="welcome"
print(strslice[1:4]) #slice from 1 and end before 4
print(strslice[4:])   #slice from 4 to end
print(strslice[-5:-1]) #slice from end -1 


"""escape characters"""
#expand tab space between letters with /t
strtb="g\to\tk\tu\tl".expandtabs(2);
print(strtb)

#singel inside single quotes
#strdb='it's right'       will throw error
print('isn\'t right')

#back slash
print("first \ will delete second \ in \\")

#\n shifts welocme to new line
print("hello\nwelcome")

print("\n")
#deletes everything before \r and prints the rest to next line
print("welcome\rworld")

#octal value of chars
print("\110 110","\n\145 145")

#hexa number
print("\x48 x48","\n \x65 x65")
