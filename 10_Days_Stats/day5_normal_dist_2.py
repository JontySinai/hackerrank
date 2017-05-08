# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

from math import erf, sqrt

# inp = raw_input()

inp = '70 10\n 80\n 60'

inp = inp.split(' ')

inp[1] = inp[1].replace('\n', '')
inp[2] = inp[2].replace('\n', '')

mean = float(inp[0])
std_dev = float(inp[1])

high_mark = float(inp[2])
pass_mark = float(inp[3])

def cum_normal(x, mean, std_dev):
    """
    Calculates the cumulative probability of any normally distributed andom variable x
    with given mean and standard deviation.

    Where the cumuluative probability is given by P(X <= x)
    """

    return 0.5*(1 + erf((x - mean)/(std_dev*sqrt(2)))) 


print round( 100 - 100*cum_normal(high_mark,mean,std_dev) ,2)
print round( 100 - 100*cum_normal(pass_mark,mean,std_dev) ,2)
print round( 100*cum_normal(pass_mark,mean,std_dev) ,2)

