# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

from math import factorial
# inp = raw_input()

inp = '12 10'

inp = inp.split(' ')

p_def = float('0.'+inp[0])

batch_size = int(inp[1])

def nCr(n, r):
    """
    Returns the number of combinations of choosing r items from a set
    of size n.
    """
    if r > n:
        return 0
    else:
        return factorial(n)/(factorial(r)*factorial(n-r))


def bi_dist(x,n,p):
    """
    Calculates the probability of exactly x successes out of n trials, where
    x is binomially distributed with P(success) = p
    """

    nCx = nCr(n, x)
    q = 1 - p

    b = nCx*(p**x)*(q**(n-x))

    return b

def bi_at_least(x,n,p):
    """
    Calculates the probability of accumulating at least x successes in n trials
    of a binomially distributed random variable with P(success) = p
    """

    b = 0
    for r in range(x, n +1):
        b += bi_dist(r,n,p)

    return b


def bi_at_most(x,n,p):
    """
    Calculates the probability of accumulating at most x successes in n trials
    of a binomially distributed random variable with P(success) = p
    """

    b = 0
    for r in range(0, x + 1):
        b += bi_dist(r,n,p)

    return b


print round(bi_at_most(2,batch_size,p_def),3)
print round(bi_at_least(2,batch_size,p_def),3)