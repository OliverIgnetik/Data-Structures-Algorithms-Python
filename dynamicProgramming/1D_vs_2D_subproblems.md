# 1D Subproblems vs. 2D Subproblems

A common question one may have while coming up with dynamic programming algorithms is "what determines the dimensions of the subproblem cache".

What differentiates the problem of longest common subsequence which has a `len(s1) x len(s2)` cache from The Change Making Problem which only requires a 1D array to cache the minimum coins to make change for amount n.

It all comes down to the **signature of the subproblem**. We discuss how different algorithms have different inputs that uniquely identify a subproblem and its corresponding solution.

## Change Making Problem (1D subproblem)

Find the minimum number of ways to make change for a given amount.
coins = [1,2,3], amount = 4

### Initializing cache

```Python
cache = [0, None, None, None, None]
```

### Approach

1. Base case is o which we just set to 1
2. Bottom up approach were we consider at each position:

- what is the best answer to make change given the current value?
- essentially we have the relation which we want to test for each coin
  ie. we iterate over the coins and try to find the best minimum for each of the related
  sub-problems that eventuate
  `1 + opt[i- coins[j]]`

**KEY TAKEAWAY: there is a single input into the opt function (amount)**
This is why the cache is 1D

## Knapsack 0/1 Problem (2D subproblem)

| Value | Weight |
| ----- | ------ |
| 60    | 5      |
| 50    | 3      |
| 70    | 4      |
| 30    | 2      |

maxWeight = 5

Maximize value while staying under maxWeight

### Approach

1. We can use an item or refuse to use that item. Either way we have one less item to consider. However, we do not take into account the weight constraint.
2. The optimum choice function has **two parameters** n = item and W = weight
   `opt(n, W)`
3. The choice becomes:

Opt(n, W) =

```
   if the weight makes the total greater then the weight constraint :

    V[i-1][w]

   otherwise pick the maximum of choosing the item (going up a row and subtracting the weight w_i) and adding the value v_i and disgarding it (going up a row):

   max(V[i-1][w], V[i-1][w-w_i] + v_i)
```

ie.
