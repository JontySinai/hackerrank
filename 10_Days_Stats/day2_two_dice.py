# Toss two unbiased die, what is the probability that there sum is at most x?

dist = [] # initialise distribution

for i in range(1,7):
    for j in range(1,7):
        dist.append(i + j)

def at_most(x):
    """
    Counts the number of occurences elements in the distribution
    of the sum of two unbiased die, which are at most x
    """

    occur = 0
    for sum in range(2,x+1):
        if sum <= x:
            occur += dist.count(sum)
    
    return occur

print at_most(9)

