# A double-ended queue, or deque, supports adding
# and removing elements from either end

import collections

d = collections.deque('abcdefg')

print 'Deque:', d
print 'Length:', len(d)
print 'Left end:', d[0]
print 'Right end:', d[-1]

d.remove('c')

print 'remove(c):', d

# Extend Left
d.extendleft(6)

# Use pop() to remove an item from the right end of the deque
# and popleft() to take from the left end

# Rotating the deque to the right (using a positive rotation) takes
# items from the right end and moves them to the left end.
