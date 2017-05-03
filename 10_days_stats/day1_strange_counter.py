#!/bin/python

import sys


# t = int(raw_input().strip())

# t = 999999997668

t = 45

init_val = 3
val = 3
for s in range(1,t+1):

    if s == t:
        break

    if val == 1:
        init_val = 2*init_val
        val = init_val
        s += 1   
    else:
        val += -1
        s += 1
        
print val


    
