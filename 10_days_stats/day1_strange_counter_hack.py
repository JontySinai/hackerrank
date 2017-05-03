""" 
Special thanks to ynyeh0221 (https://github.com/ynyeh0221/HackerRank/blob/master/Strange%20Counter.py)

I've elucidated ynyeh0221's code here by explaining the hack and renaming the variables for better readibility. 

We know that for a given time t, we only care about counting down from the last restart time (taking t = 1 as the
0th restart time). So a good strategy would be to calculate the value of the counter from the last restart time
before t.

Note that the restart times T = {1, 4, 10, 22, ...} follow the sequence 

                                    T(n) = 1 + 3*(2**(n) - 1),
                                    n = 0,1,2,3, ...

where n is the number of restart times. We could calculate when the sequence restarts by checking if the input 
value t is in the sequence but that is computationally expensive, so instead we use the simple rule that whenever 
t is a restart time, the value of the counter is always greater than the restart time. For example if we use 
(t,v) to represent a time-value tuple:

                                    (1,3), (4,6), (10,12), ... etc

And that this condition is not true whenever we are in the countdown portion of the counter:

                            (2,2), (3,1), (5,5), (6,4), (14, 8), ... etc

We will use this logic to establish whether we are at a restart time or not.

Now looking more closely at the restart values R = {3, 6, 12, ... } - note that the restart values are the differences 
between the restart times, which elucidates the sequence T(n) - we see that the restart values increase according to the 
geometric series:

                                    T(n) = 3*(2**(n)),
                                    n = 0,1,2,3, ...

Now we will use the rule value < t (if value = t, then we are simply one count away from the restart value), to
increment the counter to the next restart value. Once this condition fails (ie. value >= t), then we can check 
the value by counting down from the last restart value using the rule:

                                    val(t, n) = R(n) - (t - T(n)),
                                    n = 0,1,2,3, ...

 This leaves the problem of determining n, the number of restarts, as a function of t. We could do this analytically
 (see day1_strange_counter_rec) but this is computationally expensive so instead we use a while loop to implicitly count
 the number of restarts as long as value < t. This while loop will terminate as soon as value > t, at which point we are
 at the last restart time and the number of iterations of the while loop is equal to n.

 Note that if we start with R(0) = 3, then multiplying the restart value by 2 on every iteration of the while loop is
 identical to calculating R(n). 

 Having done this we can now proceed to calculate the value at t by noting that:

                                   t - T(n) = t - 1 - R(n-1)

So, 

                                    val(t,n) = T(n) - t + 1 + R(n-1)

which is effectively what we do in the last step.

"""

#!/bin/python

import sys
t = int(raw_input())

# set the start value to 0 so that the condition is always true for any integer t > 1
val = 0

# set the initial restart value to 3; DR0) = 3
next_restart_val = 3

# check if we are in the countdown portion, ie when value < t
while val < t:
    # increment the value by D_n so that the while loop implicitly counts restarts
    val += next_restart_val
    # implicitly calculate the next restart value using the number of iterations of the while loop
    next_restart_val *= 2


# when the while loop terminates, we will have counted the next restart value after t, so go back to the last restart value
last_restart_val = next_restart_val/2
# After the while loop terminates, value is actually equal to the sum of all the restart values, so we remove the last restart value which we have over-counted
val = val - last_restart_val

# note that at this point val is dependent on n and not on t itself, so now we use the last equation above to calculate val as a function of t

val = val - t + 1 + last_restart_val

print val



