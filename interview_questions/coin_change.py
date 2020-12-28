# number of ways to make up target value

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


print(solution(10, [1, 2, 5]))
