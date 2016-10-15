"""
For the one Pythagorean triple where a + b + c = 1000, find product a * b * c.

No tricks besides using xrange over range for this one. Brute force in ~35
seconds is sufficient for now.
"""

GOAL_SUM = 1000


def find_triple():
    for a in xrange(GOAL_SUM):
        for b in xrange(GOAL_SUM):
            for c in xrange(GOAL_SUM):
                if c > b > a:
                    if a**2 + b**2 == c**2:
                        if a + b + c == GOAL_SUM:
                            return a, b, c


def main():
    a, b, c = find_triple()
    print(a * b * c)


if __name__ == '__main__':
    main()
