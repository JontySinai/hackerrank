#!/bin/python

import sys

s = [0]

while len(s) <= 1000:   # 10 iterations: grows at rate 2^n

    t = []
    for i in range(0,len(s)):
        t.append(1 - s[i])

    s.extend(t)

def duplication(x):
    return s[x]

q = int(raw_input().strip())
for a0 in xrange(q):
    x = int(raw_input().strip())
    result = duplication(x)
    print(result)


