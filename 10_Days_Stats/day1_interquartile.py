# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

# inp = sys.stdin.readlines()

inp = ['6\n', '6 12 8 10 20 16\n', '5 4 3 2 1 5']

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

n = int(inp[0].replace('\n',''))
data = inp[1].split(' ')
data[-1] = data[-1].replace('\n','')
data = map(float, data)
freq = map(int, inp[2].split(' ')) 

freq_data = []
for i in range(0,n):
    for j in range(0,freq[i]):
        freq_data.append(data[i])

freq_data = sorted(freq_data)
N = sum(freq)
mid = N/2

if N%2 == 0:
    l_half = freq_data[0:mid]
    u_half = freq_data[mid:-1]
else:
    mid = int(mid)
    l_half = freq_data[0:mid]
    u_half = freq_data[mid + 1: -1]

Q1 = get_median(l_half, n = mid)
Q3 = get_median(u_half, n = mid)

interquartile_range = Q3 - Q1

print round(interquartile_range,1)
