"""
Implementations of 0-1 Knapsack Problem

In the knapsack problem, you are given a set of objects that have weights and
values and a knapsack that holds a certain amount of weight. Your goal is to find
the items with the maximum value that will fit in the knapsack.

@Params
Inputs : values array and weights array
Output : returns the maximum value that fits in the knapsack

NOTE: this is a 0/1 problem because we can not subdivide the potential items

References
- https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
- https://www.youtube.com/watch?v=qOUsP4eoYls&list=PLyEvk8ZeQDMVbsg7CEfT0NV3s3GkMx1vN&index=10
"""


"""
Naive approach 
Complexity 
Time : O(2^N)
Space : O(1)
"""


def knapSack_naive(W, wt, val, n):

    # Base Case
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (wt[n - 1] > W):
        return knapSack_naive(W, wt, val, n - 1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            val[n - 1] + knapSack_naive(
                W - wt[n - 1], wt, val, n - 1),
            knapSack_naive(W, wt, val, n - 1))


"""
A Dynamic Programming based Python Program for 0-1 Knapsack problem
Returns the maximum value that can be put in a knapsack of capacity W

Time : O(N*W)`psuedo polynomial time
Space : O(W)

Where W is the number of weight elements
"""


def knapSack_optimized(W, wt, val, n):
    dp = [0 for i in range(W + 1)]  # Making the dp array

    for i in range(1, n + 1):  # taking first i elements
        for w in range(W, 0, -1):  # starting from back,so that we also have data of
            # previous computation when taking i-1 items
            if wt[i - 1] <= w:
                # finding the maximum value
                dp[w] = max(dp[w], dp[w - wt[i - 1]] + val[i - 1])

    return dp[W]  # returning the maximum value of knapsack


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

print(knapSack_naive(W, wt, val, n))
print(knapSack_optimized(W, wt, val, n))
