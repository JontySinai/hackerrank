# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

from math import factorial, exp

# inp = raw_input()

inp = '2.5\n 5'

inp = inp.split(' ')

inp[0] = inp[0].replace('\n', '')

mean = float(inp[0])

k = int(inp[1])

def poisson_prob(mean, k):
    """
    Calculates the probability of obtaining k successes of Poisson distributed random variable 
    with a known mean number of successes.
    """

    p = ((mean**k)*exp(-mean))/factorial(k)

    return p


print round( poisson_prob(mean,k),3)
