"""
Suppose a family has two children, one of which is a boy. What is the probability that both children are boys?

We know that the first child is a boy, so

    P(both boys| one is a boy) = P(both boys)/P(one is a boy)
"""

genders = ['boy', 'girl']

perm = []

for first_gender in genders:
    for second_gender in genders:
        perm.append((first_gender, second_gender))

# perm = [('boy', 'boy'), ('boy', 'girl'), ('girl', 'boy'), ('girl', 'girl')]

"""
We see that P(both boys) = 1/4

and P(one is boy) = 3/4

So P(both boys | one is a boy) = (1/4)/(3/4) = 1/3 > P(both boys)
"""