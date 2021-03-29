import phonenumbers

from mobile import number

from phonenumbers import geocoder

ch_num=phonenumbers.parse(number,"CH")

print(geocoder.description_for_number(ch_num,"en"))

from  phonenumbers import  carrier
ser_num=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(ser_num,"en"))



