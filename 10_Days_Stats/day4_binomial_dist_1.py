# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

from math import factorial
# ratio_inp = raw_input()

ratio_inp = '1.09 1'

ratio = ratio_inp.split(' ')

ratio = map(float, ratio)

p_boy = ratio[0]/sum(ratio)

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

def cum_bi_dist(x,n,p):
    """
    Calculates the probability of accumulating at least x successes in n trials
    of a binomially distributed random variable with P(success) = p
    """

    b = 0
    for r in range(x, n +1):
        b += bi_dist(r,n,p)

    return b

print round(cum_bi_dist(3,6,p_boy), 3)