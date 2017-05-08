# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

from math import erf, sqrt

# inp = raw_input()

inp = '100\n 500\n 80\n 0.95\n 1.96'

inp = inp.split(' ')

inp[0] = inp[0].replace('\n', '')
inp[1] = inp[1].replace('\n', '')
inp[2] = inp[2].replace('\n', '')
inp[3] = inp[3].replace('\n', '')

n = float(inp[0])
mean = float(inp[1])
std_dev = float(inp[2])
p_val = float(inp[3])
z_score = float(inp[4])

A = mean - z_score*(std_dev)/sqrt(n)
B = mean + z_score*(std_dev)/sqrt(n)

print round(A,2)
print round(B,2)

