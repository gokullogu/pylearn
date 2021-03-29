#get elements from an array
getelem = np.array([120, 130, 140, 150, 160])
print(getelem[0], "", getelem[1])
#250

#get the elements from 2d array  [x,y]
array2d = np.array([[10, 90, 34, 78, 56], [21, 45, 78, 93, 24]])
print(array2d[0, 3])
#78

#accessing from 3d array
array3d = np.array([[[12, 12], [13, 11]], [[10, 78], [10, 22]]])
print(array3d[1, 1, 1])
#22

#using negative index to print last element
print(array3d[-1, -1, -1])
#22
