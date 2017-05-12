# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

from math import sqrt
from operator import mul as multiply
from operator import sub as subtract
from operator import pow as exponent

# inp = sys.stdin.readlines()

inp = ['10\r\n', '10 9.8 8 7.8 7.7 1.7 6 5 1.4 2 \r\n', '200 44 32 24 22 17 15 12 8 4']

n = int(inp[0].replace('\r\n',''))
X = map(float, inp[1].replace(' \r\n','').split(' '))
Y = map(float, inp[2].split(' '))

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


def get_rank(data, n):
    temp = data
    rank = range(0,n)
    max_hack = max(temp) + 1
    counter = 1
    for i in range(0,n):
        next_min = min(temp)
        pos = temp.index(next_min)
        temp[pos] = max_hack
        rank[pos] = counter
        counter += 1
    return rank


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


def spearman_rank_co(X,Y,n):
    """
    Returns the Spearman Rank Coefficient of two random variables, X and Y, with the
    same number of observations, n.
    """

    rank_X = get_rank(X, n)
    rank_Y = get_rank(Y, n)

    return pearson_cor_co(rank_X, rank_Y, n)

def spearman_rank_unique(X,Y,n):
    """
    Returns the Spearman Rank Coefficient of two random variables, X and Y, with the
    same number of observations, n, and unique values in each set of observations. This 
    method uses a special case of the rank coefficient.
    """

    rank_X = get_rank(X, n)
    rank_Y = get_rank(Y, n)

    twos = [2]*n
    diff = map(exponent, map(subtract, rank_X, rank_Y), twos)

    return 1 - 6*float(sum(diff))/(n*(n**2 - 1))

# print round(spearman_rank_co(X, Y, n), 3)
print round(spearman_rank_unique(X, Y, n), 3)