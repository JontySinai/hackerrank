# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

from math import erf, sqrt

# inp = raw_input()

inp = '250\n 100\n 2.4\n 2.0'

inp = inp.split(' ')

inp[0] = inp[0].replace('\n', '')
inp[1] = inp[1].replace('\n', '')
inp[2] = inp[2].replace('\n', '')

tickets = float(inp[0])
students = float(inp[1])
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


"""
If there are 250 tickets available and the number of tickets bought by students has a mean of 2.4 and 
standard deviation of 2.0, then calculating the probability that 100 students will be able to buy at least 1
ticket before the tickets run out is equivalent to:

    P(X <= 250 | n)

    X = no. of tickets bought by n students. 

Obviously if X > 250, then the tickets will run out before all n students have a chance to buy them. 

"""

print round( clt_cum_normal(tickets,mean,std_dev,students) , 4)
