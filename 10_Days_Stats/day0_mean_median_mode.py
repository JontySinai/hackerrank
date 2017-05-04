# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

from collections import Counter

# inp = sys.stdin.readlines()

inp = ['10\n', '64630 11735 14216 99233 14470 4978 73429 38120 51135 67060']

# get number of data points from STDIN and convert to integer type
n = int(inp[0].replace('\n',''))

# get data and store as an array
data = map(float, inp[1].split(" "))

def get_mean(data, n=-1):
    """
    Returns the mean of a list of data points with length n
    """

    if isinstance(data, str):
        data = map(float, data.split(" "))
    
    if n == -1: #if no n is specified, get n from length of array
        n = len(data)
    
    return round((sum(data)/n),1)


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

    return (sorted_data[mid-1] + sorted_data[mid])/2

    
def get_mode(data):
    """
    Returns the mode of a list of data points with length n
    """
    
    counted_data = Counter(data).most_common() # count occurences of every unique data point
    counts = zip(*counted_data)[1] # retrieve only the counts
    mode_freq = max(counts) # get the max count which will indicate the frequency of the mode
    occurences = counts.count(mode_freq) # get the number of occurences of the mode frequency which will indicate how many candidates there are for the mode
    
    mode_candidates = Counter(data).most_common(occurences) # get the possible mode candidates (most_common(n) retrieves nth largest counts in no particular order)
    mode_candidates = zip(*mode_candidates)[0]  # retrieve only the numbers themselves and not the counts

    return int(min(mode_candidates)) # set the mode to the minimum of the mode candidates (ie the smallest number with the highest frequency)


print get_mean(data,n=n)
print get_median(data, n=n)
print get_mode(data)
