import math

def answer(x):
    """
    Take input (x) as a list of train carts 2 <= t <= 100, where each cart
    contains its int number of rabbits 0 <= n <= 1000000.  Return the maximum
    number of evenly filled train carts we can get.
    """
    MAX_RABBITS_PER_CART = 1000000

    if sum(x) <= len(x):
        # we can't even put one rabbit in each bin
        return sum(x)
    else:
        # each bin has at least one rabbit
        homeless = sum(x) % len(x)
        if homeless:
            # stuff as many homeless rabbits per bin as possible
            rabbits_per_cart = sum(x) / len(x)
            bins_lost = float(homeless) / (MAX_RABBITS_PER_CART - rabbits_per_cart)
            bins_lost = int(math.ceil(bins_lost))
            return len(x) - bins_lost
        else:
            return len(x)
