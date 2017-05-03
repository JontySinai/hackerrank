# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

# inp = sys.stdin.readlines()

inp = ['12\n', '4 17 7 14 18 12 3 16 10 4 4 12']

n = int(inp[0].replace('\n',''))
data = map(float, inp[1].split(' '))

def get_median(data, n=-1):
    """
    Returns the median of a list of data points with length n
    """
    
    if isinstance(data, str):
        data = map(float, data.split(" "))
    
    if n == -1: #if no n is specified, get n from length of array
        n = len(data)

    sorted_data = sorted(data)
    mid = n/2

    if n%2 == 0:
        med = (sorted_data[mid-1] + sorted_data[mid])/2
    else:
        med = sorted_data[int(mid)]

    return med

data = sorted(data)
mid = n/2

# get lower and upper halves of the dataset. If n is odd, we exclude the middle number
if n%2 == 0:
    l_half = data[0:mid]
    u_half = data[mid:-1]
else:
    mid = int(mid)
    l_half = data[0:mid]
    u_half = data[mid + 1: -1]

Q1 = get_median(l_half, n = mid)
Q2 = get_median(data, n = n)
Q3 = get_median(u_half, n = mid)

print int(Q1)
print int(Q2)
print int(Q3)
