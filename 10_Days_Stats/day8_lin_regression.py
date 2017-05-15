# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

from operator import methodcaller
from math import sqrt

from operator import mul as multiply

# inp = sys.stdin.readlines()

inp = ['95 85\n', '85 95\n', '80 70\n', '70 65\n', '60 70']

def get_mean(data, n=-1):
    """
    Returns the mean of a list of data points with length n
    """
    
    return round((sum(data)/n),1)


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


def lin_reg(X,Y,n):
    """
    Returns the first and second parameters of a 1-st order linear regression polynomial
    that fits the data (X,Y), with n observations.
    """
    p = pearson_cor_co(X,Y,n)
    std_X = get_std_dev(X,n)
    std_Y = get_std_dev(Y,n)
    mean_X = get_mean(X, n)
    mean_Y = get_mean(Y, n)

    b = p*(std_Y/std_X)
    a = mean_Y - b*mean_X

    return [a, b] 

n = len(inp)

X = []
Y = []
for i in range(0,len(inp)):
    inp[i] = inp[i].replace('\n','')
    inp[i] = inp[i].split(' ')
    X.append(float(inp[i][0]))
    Y.append(float(inp[i][1]))

a = lin_reg(X,Y,n)[0]
b = lin_reg(X,Y,n)[1]

print round(a + b*80, 3)