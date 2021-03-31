# a brief numpy demo from the Data Structures chapter of Fluent Python by Luciano Ramalho

# import NumPy after installing it (which my IDE did automatically).
# numpy is usually imported as np
import numpy as np

# the following is a demonstration of basic operations with 2d arrays

# build and inspect a numpy.ndarray with integers 0 to 11
a = np.arange(12)
print(a)

# inspect the dimensions of the array: this is a one-dimensional, 12 element array
print(a.shape)
# prints (12,)

# add one dimension to the array, then inspect result
a.shape = 3, 4
print(a)

print('\n')
# get row at index 2
print(a[2])

print('\n')
# get element at index 2, 1
print(a[2, 1])

print('\n')
# get column at index 1
print(a[:, 1])

# create a new array by transposing (swapping columns with rows)
print(a.transpose())
