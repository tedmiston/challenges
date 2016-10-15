"""
Sum prime numbers below 2 million.

My first approach was a brute force of keeping every prime found and for each
n where 2 <= n <= MAX checking if p was a divisor for each p saved in the list
of primes so far. This worked well up to a max of 250k (~30 seconds), but at
500k it took 118s which was more than ideal. I extrapolated that 2M would take
~1800s (= 30 min).

I refactored the prime checking out of main() into is_prime(...) which somehow
reduced tottime by ~50%% in each case, despite having many more function calls
now. My guess is some kind of caching of redundant calls by the interpreter,
which hints to a possible optimization.

Now I can do a max of 500k in 60s, and 1M in 212s, but extrapolating that 2M
would take ~740s, far longer than my preferred 60s max. At 1M, 99.9%% of
tottime is spent (unsuprisingly) in is_prime(...), so I wonder which checks I
can avoid to speed it up.

The Wikipedia article for "Prime number" [1] points out that 'trial division',
the technique I've applied without knowing its name, must only loop over n
where 2 <= n <= sqrt(n). Though this method is "slow", it's fast enough, and
simple. It drops my upper wall clock time significantly: 500k in 1s; 1M in 3s
(a ~99%% reduction); and 2M in 6s. I like it.

For MAX=2M, the sum is 142913828922.

1: https://en.wikipedia.org/wiki/Prime_number
"""

MAX = 2000000

primes = []


def is_prime(n):
    sqrt_n = n ** 0.5
    for p in primes:
        if p > sqrt_n:
            return True
        if n % p == 0:
            return False
    return True


def main():
    for n in xrange(2, MAX):
        if is_prime(n):
            primes.append(n)
    print sum(primes)


if __name__ == '__main__':
    main()
