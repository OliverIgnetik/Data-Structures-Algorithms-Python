"""
A naive recursive implementation
of 0-1 Knapsack Problem

In the knapsack problem, you are given a set of objects that have weights and
values and a knapsack that holds a certain amount of weight. Your goal is to find
the items with the maximum value that will fit in the knapsack.

inputs : values array and weights array
output : returns the maximum value that fits in the knapsack

NOTE: this is a 0/1 problem because we can not subdivide 
the potential items

References
- https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
- https://www.youtube.com/watch?v=qOUsP4eoYls&list=PLyEvk8ZeQDMVbsg7CEfT0NV3s3GkMx1vN&index=10
"""


def knapSack(W, wt, val, n):

    # Base Case
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (wt[n - 1] > W):
        return knapSack(W, wt, val, n - 1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            val[n - 1] + knapSack(
                W - wt[n - 1], wt, val, n - 1),
            knapSack(W, wt, val, n - 1))


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))
