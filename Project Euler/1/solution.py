"""
For the natural numbers (1, 1000], sum those which are a multiple of 3 or 5.
"""

print(sum([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0]))
