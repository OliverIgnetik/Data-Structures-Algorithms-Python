"""
Goal : Total number of ways to make up target value

@Params 
- Input
    - n = the target value 
    - coins = available coin denominations
- Output 
    - Total number of ways to make change from target value

Runtime
A is the amount to make change for 
D is the total denominations available to us 

Time
O(A*D)
We have to solve D subproblems A times

Space 
O(A)
We only need to store A values
"""


def solution(n, coins):

    # Set up our array for tracking results
    arr = [1] + [0] * n

    for coin in coins:
        for i in range(coin, n + 1):
            arr[i] += arr[i - coin]

    if n == 0:
        return 0
    else:
        return arr[n]


print(solution(6, [1, 2, 5]))
