# example from the Data Structures chapter of Fluent Python by Luciano Ramalho
# bisect has a pair of optional arguments, lo and hi, allowing the narrowing of the region in the sequence
# to be searched when inserting. lo defaults to 0 and hi to the len() of the sequence

# bisect is alias for bisect_right. There is a sister function called bisect_left.
# bisect_right returns an insertion point after the existing item, and bisect_left returns the position
# of the existing item, so insertion would occur before it. This makes no difference for types such as int.

import bisect
import sys
import random

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}  {2}{0:<2d}'
SIZE = 7

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        # use the bisect function to get the insertion point
        position = bisect_fn(HAYSTACK, needle)
        # build a pattern of vertical bars proportional to the offset
        offset = position * '  |'
        # print formatted row showing needle and insertion point
        print(ROW_FMT.format(needle, position, offset))


# bisect can be used to perform table lookups by numeric values, i.e. to convert test scores to letter grades
breakpoints = [60, 70, 80, 90]
grades = 'FDCBA'
def grade(score):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


# this is amazing how this can be done on one line
scores = [grade(score) for score in [55, 60, 65, 70, 75, 80, 85, 90, 95]]
print(scores)

# bisect can also be used for inserting items in a sorted sequence without disrupting the order of the sequence
# insort(seq, item) inserts item into seq so as to keep seq in ascending order

random.seed()

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print(f'{new_item:2d} -> {my_list}')

"""
if __name__ == '__main__':

    # use bisect function according to last command-line argument
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    # print header with name of function selected
    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join(f'{n:2}' for n in HAYSTACK))
    demo(bisect_fn)
"""