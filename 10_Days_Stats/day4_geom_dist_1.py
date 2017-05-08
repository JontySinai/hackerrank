# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

# inp = raw_input()

inp = '1 3\n 5'

inp = inp.split(' ')

inp[1] = inp[1].replace('\n' ,'')

num = float(inp[0])
den = float(inp[1])

p_def = num/den
inspection = int(inp[2])


def geom_dist(n,p):
    return ((p-1)**(n-1))*p


print round(geom_dist(inspection,p_def),3)

