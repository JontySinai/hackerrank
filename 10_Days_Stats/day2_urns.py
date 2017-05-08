"""
Suppose there are three urns labelled X, Y and Z. 

Urn X contains 4 red balls and 3 black balls
Urn Y contains 5 red balls and 4 black balls
Urn Z contains 4 red balls and 4 black balls

One ball is drawn from each of the three urns, what is the probability that of the three balls
drawn, 2 are red and 1 is black?
"""

X_red = 4
X_black = 3
X_total = 7

Y_red = 5
Y_black = 4
Y_total = 9

Z_red = 4
Z_black = 4
Z_total = 8

"""
P(2 red, 1 black) = P(X red, Y red, Z black) + P(X red, Y black, Z red) + P(X black, Y red, Z red)

        = P(X red)*P(Y red)*P(Z black) + P(X red)*P(Y black)*P(Z red) + P(X black)*P(Y red)*P(Z black)

        = (4/7)*(5/9)*(4/8) + (4/7)*(4/9)*(4/8) + (3/7)*(5/9)*(4/8)

        = 10/63 + 8/63 + 5/42

        = 17/42
"""