#numpy has an array object ndarray
#ndarray 50x times faster than list
#as it is strored in contimuously in memory

import numpy as np
#creating the ndarray object
arr=np.array([1,2,3,4,5])
print(arr)
#[1 2 3 4 5]

print("numpy version :",np.__version__)
#numpy version : 1.20.1

#type of object arr
print(type(arr))
#<class 'numpy.ndarray'>

#creating 0-d array, a single number in a array
zero_d=np.array(12)
print("0-d array : ",zero_d)
#0-d array :  12

#creating 1-d array,contains 0-d array as an elements
one_d=np.array([12,45,11,23,45])
print("1-d array : ", one_d)
#1-d array :  [12 45 11 23 45]

#2d array contains two 1d array as its elements
two_d=np.array([[12,34,12,44,61],[16,66,23,40,65]])
print("2-d array : ", two_d)
#2-d array :  [[12 34 12 44 61][16 66 23 40 65]]

#3d_array contains two 2d array as its elements
three_d=np.array([[[12,34,55,63,12],[12,89,55,32,45]],[[90,19,21,34,21],[90,12,88,21,23]]])
print("3-d array : ", three_d)
#3-d array :  [[[12 34 55 63 12][12 89 55 32 45]][[90 19 21 34 21][90 12 88 21 23]]]

print(zero_d.ndim)
#0
print(one_d.ndim)
#1
print(two_d.ndim)
#2
print(three_d.ndim)
#3

#creating an array with 50 dimention
fiv_darr=np.array([10,20,30,40,50],ndmin=5)
print(fiv_darr,fiv_darr.ndim)
#[[[[[10 20 30 40 50]]]]] 5









