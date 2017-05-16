#!/bin/python

"""
Ok, I don't understand complexity and sorting algorithms. 

TODO Practice on worst case scenarios
TODO Research greedy algorithms

"""

import sys

n, hit, t = [7, 8, 6]
h = [16, 19, 7, 11, 23, 8, 16]

# Here's a deterministic solution. Alternative is to use a heuristic
def getMaxMonsters(n, hit, t, h):
    shoot = h
    maxhack = max(shoot) + 1
    kills = 0
    for second in range(0, t):
        target = min(h)
        aim = h.index(target)
        shoot[aim] -= hit
        if shoot[aim] <= 0:
            shoot[aim] = maxhack
            kills += 1
    return kills
 

"""
n, hit, t = raw_input().strip().split(' ')
n, hit, t = [int(n), int(hit), int(t)]
h = map(int, raw_input().strip().split(' '))
"""
result = getMaxMonsters(n, hit, t, h)
print(result)

