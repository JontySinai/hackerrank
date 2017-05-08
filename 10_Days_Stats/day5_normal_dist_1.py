# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

from math import exp, pi, erf, sqrt

# inp = raw_input()

inp = '20 2\n 19.5\n 20 22'

inp = inp.split(' ')

inp[1] = inp[1].replace('\n', '')
inp[2] = inp[2].replace('\n', '')

mean = float(inp[0])
std_dev = float(inp[1])
Q1 = float(inp[2])
Q2_lower = float(inp[3])
Q2_upper = float(inp[4])


def std_normal(x):
    """
    Calculates the probability of a normally distributed random variable x
    with mean 0 and standard deviation 1.
    """

    return exp(-(x**2)/2)/sqrt(2*pi)


def normal(x, mean, std_dev):
    """
    Calculates the probability of any normally distributed random variable x
    with given mean and standard deviation.
    """

    return (1/std_dev)*std_normal((x - mean)/std_dev)


def cum_normal(x, mean, std_dev):
    """
    Calculates the cumulative probability of any normally distributed andom variable x
    with given mean and standard deviation.

    Where the cumuluative probability is given by P(X <= x)
    """

    return 0.5*(1 + erf((x - mean)/(std_dev*sqrt(2)))) 


print round( cum_normal(Q1,mean,std_dev) ,3)
print round( cum_normal(Q2_upper,mean,std_dev) - cum_normal(Q2_lower,mean,std_dev) ,3)
