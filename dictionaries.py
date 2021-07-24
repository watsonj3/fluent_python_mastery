# example from the Dictionaries chapter of Fluent Python by Luciano Ramalho


# There are several different ways of building a dictionary
# each of these have the same set of keys and values, even if their order is not the same.
# therefore,they are all considered equal
a = dict(one=1, two=2, three=3)
b = {'three': 3, 'two': 2, 'one': 1}
c = dict([('two', 2), ('one', 1), ('three', 3)])
d = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)

# listcomps and genexps were adapted to dict comprehensions (and set comprehensions).
# a dictcomp builds a dict instance by taking key:value pairs from any iterable.
# the following shows the use of dict comprehensions to build two dictionaries from the same list of tuples

# an interable of key-value pairs like dial_codes can be passed directly to the dict constructor.
dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States')
]
# here we swap the pairs: country is the key, and code is the value.s
country_dial = {country: code for code, country in dial_codes}
print(country_dial)

# Sorting country_dial by name, reversing the pairs again, uppercasing values, and filtering items by code < 70
print({code: country.upper()
       for country, code in sorted(country_dial.items())
       if code < 70})
