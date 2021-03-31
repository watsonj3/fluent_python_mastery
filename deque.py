# # example from the Data Structures chapter of Fluent Python by Luciano Ramalho

# using lists to .append and .pop can be expensive because the entire list must be shifted in memory

# The class collections.deque is a thread-safe double-ended queue designed for fast inserting and removing
# from both ends

from collections import deque

# optional maxlen argument sets the maximum number of items allows in this instance of deque
dq = deque(range(10), maxlen=10)
print(dq)
# rotating with n > 0 takes items from the right end and prepends them to the left.
# when n < 0, items are taken from left and appended to the right
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)

# appending to a deque that is full (len(d) == d.maxlen) discards items from the other end
dq.appendleft(-1)
# show that the 0 was removed
print(dq)
# adding three items to the right pushes out the leftmost -1, 1, and 2
dq.extend([11, 22, 33])
print(dq)
# extendleft(iter) works by appending each successive item of the iter argument to the left of the deque.
# the final position of the items are reversed
dq.extendleft([10, 20, 30, 40])
print(dq)
