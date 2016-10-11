"""
Problem 3 - Largest Prime Factor

== Usage ==

You can pass an optional integer positional arg for the number of which you
want to find the largest prime factor.  If omitted, it will default to the
number requested by the problem description.

== Background ==

This is an integer factorization [5] problem, specifically, prime
factorization.

When I started this problem I was doing a lot more work than necessary which
led to a few quick insights:

  1. In is_prime(...), there's no need to check even numbers above two because
     they're never prime [1].

  2. In is_prime(...), testing for primality is much easier computationally
     than factorization [2].As the program was already sub 1 second runtime on
     the desired input, I didn't put time into optimizing factorize(...) for
     this, but there are

  3. In factorize(...), testing only 1..floor(sqrt(n)) is much cheaper than
     redundantly going all the way to n.

== Notes ==

Note: Python 3.  This is important because the division operator was changed
to "true division" instead of "classic division" [4].

[1]: https://en.wikipedia.org/wiki/Generating_primes
[2]: https://en.wikipedia.org/wiki/Primality_test
[3]: https://en.wikipedia.org/wiki/Trial_division
[4]: https://www.python.org/dev/peps/pep-0238/
[5]: https://en.wikipedia.org/wiki/Integer_factorization
"""

import argparse
import math

DEFAULT_N = 600851475143  # the answer requested in question

parser = argparse.ArgumentParser()
parser.add_argument('n', metavar='n', type=int, nargs='?', default=DEFAULT_N,
                    help='Find the largest prime factor of this number')
args = parser.parse_args()


def is_factor(n, i):
    """Is i a factor of n (i.e., is n divisible by i)?"""
    return n % i == 0


def factorize(n):
    """Compute factors of n in descending order (e.g., n=6 --> [6, 3, 2, 1]).

    This uses trial division [3], the simplest method for testing primality.
    There are much faster methods available [2].

    I'm not crazy about building a list and having to reverse sort here.  In
    further enhancements, I would try using a generator instead to save memory
    and unnecessary cpu cycles.  Another idea would be to build a prime number
    sieve.
    """
    factors = []
    for i in range(math.floor(math.sqrt(n)), 0, -1):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n/i))
    return sorted(factors, reverse=True)


def is_prime(n):
    """Return true if n is prime; false if n is composite."""
    if n % 2 == 0 and n > 2:
        return False
    else:
        factors = factorize(n)
        return len(factors) == 2


def lpf(n):
    """What is the largest prime factor of a number?"""
    for i in factorize(n):
        if is_prime(i):
            return i
    return None  # error


def main():
    num = args.n
    result = lpf(num)
    print('lpf({}) --> {}'.format(num, result))


if __name__ == '__main__':
    main()
