"""
Naive approach
Time : O(N^2)
Space : O(K)
where K is the length of the running sub array
"""


def quadratic_approach(arr):
    maxSum = -float('inf')
    maxSub = []
    for left in range(len(arr)):
        runningWindowSum = 0
        runningSubArray = []

        for right in range(left, len(arr)):
            runningWindowSum += arr[right]
            runningSubArray.append(arr[right])
            if (runningWindowSum > maxSum):
                maxSum = runningWindowSum
                maxSub = runningSubArray[:]

    return [maxSum, maxSub]


"""
Kadane's algorithm
Time : O(N)
Space : O(K)
where K is the length of the running sub array
"""


def kadane_algorithm(arr):
    runningSum = arr[0]
    maxSum = arr[0]
    maxSub = []
    runningSub = []

    for i in range(1, len(arr)):
        if (runningSum < arr[i]):
            runningSum = arr[i]
            runningSub = [arr[i]]
        else:
            runningSum += arr[i]
            runningSub.append(arr[i])

        if runningSum > maxSum:
            maxSum = runningSum
            maxSub = runningSub[:]

    return [maxSum, maxSub]


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(kadane_algorithm(arr))
