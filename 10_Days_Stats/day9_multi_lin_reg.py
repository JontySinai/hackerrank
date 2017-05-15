# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

import numpy as np
from math import ceil

# inp = sys.stdin.readlines()

inp = ['2 7\n', '0.18 0.89 109.85\n', '1.0 0.26 155.72\n', '0.92 0.11 137.66\n', '0.07 0.37 76.17\n', '0.85 0.16 139.75\n', '0.99 0.41 162.6\n', '0.87 0.47 151.77\n', '4\n', '0.49 0.18\n', '0.57 0.83\n', '0.56 0.64\n', '0.76 0.18']

for i in range(0, len(inp)):
    inp[i] = inp[i].replace('\n','')
    inp[i] = inp[i].split(' ')

m = int(inp[0][0])
n = int(inp[0][1])

X = []
Y = []
for a_set in range(1,n+1):
    row = [1]
    row.extend(inp[a_set][0:-1])
    row = map(float, row)

    X.append(row)
    Y.append(float(inp[a_set][-1]))

X = np.array(X)
Y = np.array(Y)

XTX = np.matmul(np.transpose(X), X)

XTXinvXT = np.matmul(np.linalg.inv(XTX), np.transpose(X))

B = np.matmul(XTXinvXT, Y)

q = int(inp[n+1][0])

for test in range(n+2, n + 2 + q):
    test_case = [1]
    test_case.extend(map(float, inp[test]))

    X_new = np.array(test_case)

    Y_new = np.matmul(X_new, B)

    print round(Y_new + 0.004999, 2 )
    

