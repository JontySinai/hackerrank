# Toss two unbiased die, what is the probability that the values of the dice are different
# and their sum is 6?

dist = [] # initialise distribution
sum_six = []

for i in range(1,7):
    for j in range(1,7):
        dist.append(i + j)

        if i + j == 6:
            sum_six.append((i,j))

count = 0

for i,j in sum_six:
    if i != j:
        count += 1

perm = len(dist) # no. of permutations of tossing two die and counting the sum

"""
P(i != j and sum = 6) = P(i != j) int P(sum = 6) = 4/36 = 1/9
"""

p = float(count)/perm

print count
print perm
print p

print p - float(1)/9