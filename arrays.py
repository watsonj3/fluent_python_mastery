# example from the Data Structures chapter of Fluent Python by Luciano Ramalho

# There are other options other than lists for sequences.
# arrays can be useful depending on requirements

# an array saves a lot of memory when you need to store millions of floating point values.
# if you are constantly adding and removing items from opposite ends of a list, then a deque is a more efficient
# data structure

# sets are optimized for fast membership checking and should be preferred if you are constantly checking whether an
# item is in a collection

# arrays are useful in that it supports all mutable sequence operations, such as .pop, .insert, and .extend, and
# additional methods for fast loading and saving such as .frombytes and .tofile

# A Python array is as lean as a C array. An array of float values does not hold full-fledged float instances, but only
# the packed bytes representing their machine values, similar to an array of double in C.

# when creating an array, you provide a typecode, a letter to determine the underlying C type used to store each item
# in the array. b is the typecode for signed char. If you create an array('b'), then each item will be stored in a
# single byte and interpreted as an integer from -128 to 127. This saves a lot of memory for large sequences

# Python also checks to see if a number matches the type for the array. This will remove the source of some pesky error
# messages

# import the array type
from array import array
from random import random

# create an array of double-precision floats (typecode 'd') from any iterable object
floats = array('d', (random() for i in range(10**7)))
# examine last number in the array
print(floats[-1])

# save floats to a binary file
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

# create an empty array of doubles
floats2 = array('d')
fp = open('floats.bin', 'rb')
# read 10 million numbers from the binary file
floats2.fromfile(fp, 10**7)
fp.close()
# examine the last number in the array
print(floats2[-1])
# verify that the contents of the arrays match
print(floats2 == floats)

# the above methods of reading a file is very fast. It takes about 0.1s for array.fromfile to load 10 million
# double-precision floats from a binary file. This is nearly 60 times faster than reading the numbers from a
# text file, which also involves parsing each line with the float built-in.
# also, the size of the binary file with 10 million doubles is 80,000,000 bytes (8 bytes per double, zero overhead)
# the same text file has 181,515,739 bytes, for the same data.

# memoryview lets you handle slices of arrays without copying bytes.
# memoryview.cast method lets you change the way multiple bytes are read or written as units without moving bits around.
# memoryview.cast returns yet another memoryview object, always sharing the same memory

# build an array of 6 bytes
octets = array('B', range(6))
# build memoryview from that array, then export it as a list
m1 = memoryview(octets)
m1.tolist()
print(m1)
# build new memoryview from the previous one, but with 2 rows and 3 columns
m2 = m1.cast('B', [2, 3])
m2.tolist()
print(m2)
# build another memoryview with 3 rows and 2 columns
m3 = m1.cast('B', [3, 2])
m3.tolist()
print(m3)
# overwrite byte in m2 at row 1, column 1 with 22
m2[1, 1] = 22
# overwrite byte in m3 at row 1, column 1 with 33
m3[1, 1] = 33
# display original array, proving that the memory was shared among octets m1, m2, and m3
print(octets)

# you can also use memoryview to corrupt memory
numbers = array('h', [-2, -1, 0, 1, 2])
# build a memoryview from an array of 5 16-bit signed integers (typecode 'h')
memv = memoryview(numbers)
print(memv)
# prove that memv sees the same 5 items in the array
print(len(memv))
print(memv[0])
# create memv_oct by casting the elements of memv to bytes (typecode 'B')
memv_oct = memv.cast('B')
# export elements of memv_oct as a list of 10 bytes to view
memv_oct.tolist()
print(memv_oct)
# Assign value 4 to byte offset 5
memv_oct[5] = 4
# a 4 in the most significant byte of a 2-byte unsigned integer is 1024
print(numbers)