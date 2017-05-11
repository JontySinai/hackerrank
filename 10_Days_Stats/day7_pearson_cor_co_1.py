# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

from operator import mul as multiply
from math import sqrt

# inp = sys.stdin.readlines()

inp = ['10\r\n', '10 9.8 8 7.8 7.7 7 6 5 4 2 \r\n', '200 44 32 24 22 17 15 12 8 4']

def get_mean(data, n=-1):
    """
    Returns the mean of a list of data points with length n
    """
    
    return round((sum(data)/n),1)


def get_std_dev(data, n):
    """
    Returns the standard deviation of a list of data points with length n
    """
    mean = get_mean(data, n)

    deviations = []

    for i in range(0,n):
        deviations.append( (data[i] - mean)**2 )

    std_dev = sqrt( sum(deviations)/n )

    return std_dev


def pearson_cor_co(X, Y, n):
    """
    Returns the Pearson Correlation Coefficient of two random variables, X and Y, with
    the same number of observations, n.
    """

    mean_X = get_mean(X,n)
    mean_Y = get_mean(Y,n)

    std_X = get_std_dev(X,n)
    std_Y = get_std_dev(Y,n)

    err_X = []
    err_Y = [] 
    for i in range(0,n):
        err_X.append(X[i] - mean_X)
        err_Y.append(Y[i] - mean_Y)

    return sum(map( multiply, err_X, err_Y))/(n*std_X*std_Y)


n = int(inp[0].replace('\r\n',''))
X = map(float, inp[1].replace(' \r\n','').split(' '))
Y = map(float, inp[2].split(' '))

print round(pearson_cor_co(X,Y,n), 3)
