"""
The manager of an industrial plant is planning on buying a machine of either type A or B. For each day's operation:

-   The number of repairs X, that Machine A needs, is a Poisson distributed random variable with mean 0.88. The daily
    cost of operating A is given by:

        C_A = 160 + 40X^2

-   The number of repairs Y, that Machine B needs, is a Poisson distributed random variable with mean 1.55. The daily
    cost of operating B is given by:

        C_B = 128 + 40Y^2

Now to calculate the expected daily cost of each machine, we use the fact that:

-   The expectation operator E[] is linear
-   For a Poisson distributed random variable X with mean lambda:

    E[X^2] = lambda + lambda^2

Then, 

    E[C_A] = 160 + 40(E[X^2])

    E[C_B] = 128 + 40(E[Y^2])
"""

import sys

# inp = raw_input()

inp = '0.88 1.55'

inp = inp.split(' ')

mean_A = float(inp[0])
mean_B = float(inp[1])

Exp_A = 160 + 40*(mean_A + mean_A**2)

Exp_B = 128 + 40*(mean_B + mean_B**2)

print round(Exp_A,3)

print round(Exp_B,3)

