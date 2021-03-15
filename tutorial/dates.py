import datetime

#to create an object for date
dt = datetime.datetime.now()
print(dt)
#2021-03-14 17:09:00.738904

#to print present year
print(dt.year)
#2021
#or
print(dt.strftime("%Y"))

#prints day name in short
print(dt.strftime("%a"))
#sun

#prints day name in full version
print(dt.strftime("%A"))
#sunday

#weekday as a number 0-6
print(dt.strftime("%w"))
#0

#day of month 01-31 as number
print(dt.strftime("%d"))
#14

#month name short version
print(dt.strftime("%b"))
#Mar

#month name full version
print(dt.strftime("%B"))
#March

#month as a number
print(dt.strftime("%m"))
#03

#year full version
print(dt.strftime("%y"))
#21

#24 hour time format
print(dt.strftime("%H"))
#17

#12 hour time format
print(dt.strftime("%I"))
#05

#pm/am
print(dt.strftime("%p"))
#PM

#minute
print(dt.strftime("%M"))
#39

#second
print(dt.strftime("%S"))
#43

#microsecond
print(dt.strftime("%f"))
#792485

#print(dt.strftime("%Z"))
#CST

#print date 
print(dt.strftime("%x"))
#03/4/21

#print time
print(dt.strftime("%X"))
#17:50:01

#print utf
print(dt.strftime("%j"))
#073


#print ISO 8061 year
print(dt.strftime("%G"))
#2021

#print ISO 8061 weekday
print(dt.strftime("%u"))
#7

#print ISO 8061 week number
print(dt.strftime("%V"))
#10

#create an date object
ctdt=datetime.datetime(2021,5,18)
print(ctdt)