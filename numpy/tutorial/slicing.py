import numpy as np
#takes the values from start index to end index
arr_slice=np.array([12,90,65,45,32,23,14,54,22,34])

#prints from start to end
print(arr_slice[:])
#[65 45 32 23 14 54 22 34]

#from start to 5 
print(arr_slice[:5])
#[12 90 65 45 32]

#from 5 to end
print(arr_slice[5:])
#[23 14 54 22 34]


print(arr_slice[-5:-2])
#[23 14 54]

#step moves the array with n increment default is 1
print(arr_slice[1:6:2])#2 is step value
#[90 45 23]

#print the array with 2 

