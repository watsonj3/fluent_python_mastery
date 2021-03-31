# example from the Data Structures chapter of Fluent Python by Luciano Ramalho

# To evaluate express seq[start:stop:step], Python calls seq.__getitem__(slice(start, stop, step))


l = [10, 20, 30, 40, 50, 60]
# split at 2
print(l[:2])
# [10, 20]
print(l[2:])

# split at 3
print(l[:3])

print(l[3:])



# sequences also support + and *. Usually, both operands of + must be of the same sequence type, and neither is
# modified, but a new sequence of that same type is created as a result of concatenation

l = [1, 2, 3]
print(l * 5)

# you can also multiply a sequence with an integer. A new sequence is then created.
new_sequence = 5 * 'abcd'
print(new_sequence)

# Another interesting use of slicing is the ability to assign to slices.
a = list(range(10))
print(a)
a[2:5] = [20, 30]
print(a)
# also easily delete elements in a list
del a[5:7]
print(a)
a[3::2] = [11, 22]
print(a)
# this will print out a TypeError message
# the right side must be an iterable object
# a[2:5] = 100
a[2:5] = [100]
print(a)

# The following will work with listcomp
# creates a list of three lists of three items each.
board = [['_'] * 3 for i in range(3)]
print(board)
# You can also modify a specifc row and column
board[1][2] = 'X'
print(board)

p = [1, 2, 3]
# print the id of the initial list
print(id(p))
# after multiplication, the list is the same object, with new items appended
p *= 2
print(p)
# has the same id as the initial list
print(id(p))

t = (1, 2, 3)
# print id of the initial tuple
print(id(t))
# after multiplication, a new tuple is created
t *= 2
print(id(t))

# repeated concatenation of immutable sequences is inefficient, because instead of just appending new items,
# the interpreter has to copy the whole target sequence to create a new one with the new items concatenated.

# this is a strange corner case
# it will generate a TypeError when running in IDE
# if it runs in the console, it will have different behavior. It will have a TypeError and still modify the tuple
# h = (1, 2, [30, 40])
# h[2] += [50, 60]
# print(h)

# The above example shows how dangerous it can be to put mutable items in tuples

# let's examine the list.sort method
# The list.sort method sorts a list in-place, without making a copy. It returns None to remind us that it changes the
# receiver, and does not create a new list.
# This is an important Python API convention: functions or methods that change an object in-place should return
# None to make it clear to the caller that the receiver was changed, and no new object was created.
# random.shuffle(s) function does the same thing. It shuffles the mutable sequence in place, and returns None.

# the build-in functgion sorted creates a new list and returns it. It accepts any iterable object as an argument,
# including immutable sequences and generators. It always returns a newly created list

# Both list.sort and sorted take two optional, keyword-only arguments: reverse and key

fruits = ['grape', 'raspberry', 'apple', 'banana']
sorted(fruits)
print(fruits)
# produce a new list of strings sorted alphabetically
print(sorted(fruits))
# reverse previous alphabetical ordering
print(sorted(fruits, reverse=True))
# sort in descending order of length.
print(sorted(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))
# the ordering of the original fruits list has not changed
print(fruits)
# This sorts the list in place, and returns None (which the console omits)
fruits.sort()
# Now, the original fruits list is sorted
print(fruits)

# Once lists are sorted, then they can be efficiently searched.
# Binary search algorithm is provided in the bisect module of the standard library

# the bisect module provides two main functions -- bisect and insort -- that uses binary search to
# quickly find and insert items in any sorted sequence
