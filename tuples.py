# example from the Data Structures chapter of Fluent Python by Luciano Ramalho
import os
# Tuples

# Tuples can be used as immutable lists and also as records with no field names

# Tuples can hold records: each item in the tuple holds the data for one field and the
# position of the item gives it meaning
# when used as a collection of fields, the number of items is usually fixed, and their order is always important

# latitude and longitude of LAX
lax_coordinates = (33.9425, -118.408056)

# data about Tokyo: name, year, population (thousands), population change(%), area(km^2)
# example of unpacking
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)

# a list of tuples of the form (country_code, passport_number)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),
                ('ESP', 'XDA205')]
# as we iterate over the list, passport is bound to each tuple
for passport in sorted(traveler_ids):
    # The % formatting operator understands tuples and treats each item as a separate field
    print('%s/%s' % passport)

# The for loop knows how to retrieve the items of a tuple separately
# called unpacking. Assigned to _, a dummy variable
for country, _ in traveler_ids:
    print(country)

# Tuple unpacking works with any iterable object. Iterable yields exactly one item pervariable in the receiving tuple
# unless you use *

# parallel assignment
latitude, longitude = lax_coordinates
print(latitude)

# use * to unpack
# alo shows you can enable functions to return multiple values
print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))
quotient, remainder = divmod(*t)
print(quotient, remainder)

# the os.path.split() function builds a tuple (path, last_part) from a filesystem path
# if we only care about certain parts of a tuple when unpacking, use a dummy variable, '_'
_, filename = os.path.split('/home/luciano/.ssh/id_rsa.pub')
print(filename)

# use * to grab excess items
# define function parameters with *args to grab arbitrary excess arguments

a, b, *rest = range(5)
print(a, b, rest)
a, b, *rest = range(3)
print(a, b, rest)
a, b, *rest = range(2)
print(a, b, rest)

# the * prefix can appear in any position
a, *body, c, d = range(5)
print(a, body, c, d)
*head, b, c, d = range(5)
print(head, b, c, d)

# tuples use less memory than a list of the same length. You also know that a tuples length will never change.
# immutability in a tuple only applies to the references contained in it. References in a tuple cannot be deleted or
# replaced. If one of these references point to a mutable object, and that object is changed, then the value of the
# tuple changes.

# the list in the tuple is mutable and can be changed
# this can be a source of bugs
a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])
print(a == b)
b[-1].append(99)
print(a == b)
print(b)

# if you want to make sure a tuple remains unchanged, you can compute its hash.
# an object is only hashable if its value cannot ever change.

def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True


# returns True
tf = (10, 'alpha', (1, 2))
# returns False
tm = (10, 'alpha', [1, 2])
print(fixed(tf))
print(fixed(tm))





# tuple unpacking also works with nested structures

# each tuple holds a record with four fields, the last of which is a coordinated pair
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f'{"":15} | {"lat.":^9} | {"long.":^9}')
    # assign the last field to a nested tuple and unpack the coordinates
    # limit output to metropolitan areas in the Western hemisphere
    for name, cc, pop, (latitude, longitude) in metro_areas:
        if longitude <= 0:
            print(f'{name:15} | {latitude:9.4f} | {longitude:9.4f}')

if __name__ == '__main__':
    main()