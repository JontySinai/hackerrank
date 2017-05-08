# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

from math import erf, sqrt

# inp = raw_input()

inp = '9800\n 49\n 205\n 15'

inp = inp.split(' ')

inp[0] = inp[0].replace('\n', '')
inp[1] = inp[1].replace('\n', '')
inp[2] = inp[2].replace('\n', '')

max_weight = float(inp[0])
n = int(inp[1])
mean = float(inp[2])
std_dev = float(inp[3])

def clt_cum_normal(x, mean, std_dev, n):
    """
    Calculates the cumulative probability of any normally distributed andom variable x
    with given mean and standard deviation using the Central Limit Theorem

    Where the cumuluative probability is given by P(X <= x)
    """

    clt_mean = n*mean
    clt_std_dev = sqrt(n)*std_dev

    return 0.5*(1 + erf((x - clt_mean)/(clt_std_dev*sqrt(2)))) 


print round( clt_cum_normal(max_weight,mean,std_dev,n) , 4)

