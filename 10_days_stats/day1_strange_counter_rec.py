#!/bin/python

import sys

import math


# t = int(raw_input().strip())

# t = 999999997668

t = 11

"""
The numbers for restarting the counter are:

    S = {1, 4, 10, 22 ... } 

The differences are:

    D = {3, 6, 12 ... } 

The sequence D is clearly a geometric series with ratio r = 2 and initial value a = 3. 
So the formula for D(n), where n in |N, is :

    D(n) = (a/r-1)*(r^(n)-1)
         
         = 3*(2**(n)-1)

Starting at 1, to get the nth term in S we add D(n-1), so:

    S(n) = 1 + D(n-1)

         = 1 + 3*(2**(n-1)-1)

"""

def diff(n):
    """
    Sequence for the differences D(n) = 3*(2**(n)-1)
    """
    d_n = 3*(2**(n-1))
    return d_n

def seq(n):
    """
    Sequence for S(n) = 1 + 3*(2**(n-1)-1)
    """
    s_n = 1 + 3*(2**(n-1)-1)
    return s_n

def check_seq(y):
    """
    Checks if y is in the sequence S{1, 4, 10, ...}
    where S(n) = 1 + 3*(2**(n-1)-1). 

    If n is an intger, then y is in the sequence.
    """
    x = (y+2)/3 
    n = math.log(x,2) + 1

    if seq(n) == y:
        if n.is_integer():
            return True, n
        else:
            return False
    else:
        return False

def find_restart(t):
    """
    Finds the previous restart time s, to the input time t
    """

    if check_seq(t):
        r = t
    else: 
        while not check_seq(t):
            t += -1
        r = t
    
    return r


def get_init(restart_incidence):
    """
    Given a restart value r, find the initial value of the countdown
    """
    init_val = diff(restart_incidence)
    return init_val

r = find_restart(t)
restart_incidence = check_seq(r)[1]
init_val = get_init(restart_incidence)
val = init_val

for s in range(r,t+1):

    if s == t:
        break

    val += -1
    s += 1
    
print int(val)   
