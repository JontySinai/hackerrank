# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
from operator import mul as multiply

# inp = sys.stdin.readlines()

inp = ['5\n', '10 40 30 50 20\n', '1 2 3 4 5']

n = int(inp[0].replace('\n',''))

data = map(float, inp[1].split(' '))

weights = map(float, inp[2].split(' '))

w_mean = (sum(map(multiply, data, weights)))/(sum(weights))

print round(float(w_mean),1)