import array

# example from the Data Structures chapter of Fluent Python by Luciano Ramalho

# example of using list comprehension to iterate through a list
# List comprehensions build lists from sequences or any other iterable type by filtering and transforming items.
symbols = '#$%^&*(*'
codes = [ord(symbol) for symbol in symbols]
print(codes)


# here is a slower and less efficient way to iterate through this list
# the first example is more readable, and more efficient and should be preferred.
codes1 = []
for symbol in symbols:
    codes1.append(ord(symbol))

print(codes1)


# Listcomps vs map and filter
# listcomps do everything the map and filter functions do.

beyond_ascii = [ord(s) for s in symbols if ord(s) > 40]
print(f"Beyond_ascii: {beyond_ascii}")
beyond_ascii = list(filter(lambda c: c > 40, map(ord, symbols)))
print(f"Beyond_ascii using map and filter: {beyond_ascii}")

# list comprehension can build lists from the Cartesian product of two or more iterables.
# The items that make up the cartesian product are tuples made from items from every input iterable.
# The resulting list has a length equal to the lengths of the input iterables multiplied.

# Here is an example:
# We need to produce a list of T-shirts available in two colors and three sizes. Here is an example
# to produce a list using listcomp.  Keep in mind that listcomp's generate lists.

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
# generate a list of tuples arranged by color, then size
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

for color in colors:
    for size in sizes:
        print((color, size))

# arrange list by size, then color. Note you can have a line break.
tshirts = [(color, size) for size in sizes
           for color in colors]
print(tshirts)

# use genexps to build a tuple and an array


print(tuple(ord(symbol) for symbol in symbols))

# array constructor takes two arguments, so the parentheses around the generator expression are mandatory
# first argument of the array constructor defines the storage type used for the numbers in the array
print(array.array('I', (ord(symbol) for symbol in symbols)))

# use genexp with a Cartesian product to print out a roster of T-shirts of two colors in three sizes.
# the size-item list of T-shirts is never built in memory: the generator expression feeds the for loop producing one
# item at time. If the two lists used in Cartesian product was huge, using a genexp would save the cost of building a
# giant list.
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)