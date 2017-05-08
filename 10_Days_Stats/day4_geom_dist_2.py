"""
Suppose that the probability that a machine produces a defective product is 1/3. 
What is the probability that the first defect is found during the first 5 inspections?

There are 6 possible cases:

- Case 1 - 5: The first defect is found in the i-th Case, i = 1:5
- Case 6: No defects are found in the first 5 inspections

Now

    P(first defect found in first 5 inspections) = 1 - P(no defects found in the first 5 inspections)

And if p_def = 1/3, then p_no_def = 2/3 so

    P(no defects found in the first 5 inspections) = (2/3)**5

Thus

    P(first defect found in first 5 inspections) = 1 - (2/3)**5

"""

import sys

# inp = raw_input()

inp = '1 3\n 5'

inp = inp.split(' ')

inp[1] = inp[1].replace('\n' ,'')

num = float(inp[0])
den = float(inp[1])

p_def = num/den
inspection = int(inp[2])


p_no_def = 1 - p_def

p_no_def_after_inspection = p_no_def**inspection

print round(1 - p_no_def_after_inspection, 3)

