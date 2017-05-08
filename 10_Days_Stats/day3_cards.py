"""
Draw two cards from a standard 52 deck without replacement.
What is the probability that the cards are the same suit.BaseException
"""

"""
P(both draws same suit) = P(second draw suit matches first | first draw's suit)

                    = P(same suit)/P(first draw's suit)

Now P(first draw's suit) = 13/52 = 1/4 (13 choices from 52 cards)

P(second draw's suit) = 12/51 (got 12 choices left from 51 cards)

Now if we go through the algebra:

P(same suit) = P(second draw's suit)*P(first draw's suit)

So P(both draw's same suit) = P(second draw's suit)

                            = 12/51
"""