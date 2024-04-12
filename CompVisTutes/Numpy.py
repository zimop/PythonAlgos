import numpy as np;

##creating an array:
array = np.array([1,2,3,4])

##useful functions for populating arrays:
array_size = (2, 3)
np.arange(1, 11) #prints between 1 and 10
np.zeros(array_size) #array of zeros
np.ones(array_size) # array of ones

##to change the datatype of a numpy array:
array.astype(np.float64)
array.astype(np.float16)
array.astype(np.float8)

##indexing:
array[array>2] #boolean indexing, all values above 2
barray = np.array([[1,2,3], [4,5,6]])
barray[:,2] #prints [2, 5]. Picks all elements along the first axis (meaning all rows), and picks only the 2nd element in every row

##flattening an array:
barray.ravel() #prints [1, 2, 3, 4, 5, 6]

##reshaping an array:
barray.reshape(3, 2) #reshapes the array to 3 x 2

##appending:
np.append(array, [1, 1]) #second value must be an array.

##inserting:
np.insert(array, 2, [1, 1]) #second value is the location of where you want to put the value.

##element-wise arithmetic is always supported
