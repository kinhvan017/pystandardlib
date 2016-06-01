import collections

c = collections.Counter('abcaddaadbbccdee')

for letter in 'abcde':
    print '%s: %d' % (letter, c[letter])
# If a value has not been seen in the input (as with e in this example),
# its count is 0

# elements() turns an iterator that produces all items known to the Counter
print list(c.elements())

# most_common() to produce a sequence of the n most frequently encountered
# input values and their respective counts
