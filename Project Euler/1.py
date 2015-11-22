"""
For the natural numbers (1, 1000], find the sum of all those which are a multiple of 3 or 5.
"""

print sum([i for i in xrange(1, 1000) if i % 3 == 0 or i % 5 == 0])
