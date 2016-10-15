"""
Sum the even-valued terms in the Fibnonnaci sequence over (1, 4000000).

The trick here is definitely memoization to avoid blowing up the stack with
recursive calls.
"""

memo = {}


def memoize(func):
    """Store previously computed numbers for performance."""
    def inner(n):
        return memo[n] if n in memo else func(n)
    return inner


@memoize
def fib(n):
    """Return the nth number in the Fibonacci sequence."""
    if n == 0:
        v = 0
    elif n == 1:
        v = 1
    else:
        v = fib(n-1) + fib(n-2)
    memo[n] = v
    return v


def even(n):
    """Return True if n is even."""
    return n % 2 == 0


def main():
    STARTING_TERM = 1
    MAX_VALUE = 4000000

    result = []
    term = STARTING_TERM
    while fib(term) <= MAX_VALUE:
        result.append(fib(term))
        term += 1

    evens = [i for i in result if even(i)]
    print(sum(evens))
    assert sum(evens) == 4613732


if __name__ == '__main__':
    main()
