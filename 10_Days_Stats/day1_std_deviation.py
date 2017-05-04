# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
from math import sqrt

# inp = sys.stdin.readlines()

inp = ['5\r\n', '10 40 30 50 20']

def get_mean(data, n=-1):
    """
    Returns the mean of a list of data points with length n
    """
    mean = (sum(data)/n)

    return mean

def get_std_dev(data, n = -1):
    """
    Returns the standard deviation of a list of data points with length n
    """
    mean = get_mean(data, n =n)

    deviations = []

    for i in range(0,n):
        deviations.append( (data[i] - mean)**2 )

    std_dev = sqrt( sum(deviations)/n )

    return std_dev


n = int(inp[0].replace('\n',''))
data = map(float, inp[1].split(" "))

std_dev = get_std_dev(data, n = n)

print round(std_dev,1)