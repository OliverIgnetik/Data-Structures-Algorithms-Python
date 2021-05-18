# credit : https://www.geeksforgeeks.org/radix-sort/
# resource : https://www.youtube.com/watch?v=5n8KZnQvf4k

# Python program for implementation of Radix Sort
# A function to do counting sort of arr[] according to
# the digit represented by exp.

##################### COMPLEXITY ANALYSIS #######################################

# Time complexity O(d(n + k))
# Space complexity O(n + k)

# where n is the number of keys and k is the


def countingSort(arr, exp1):

    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i] / exp1)
        count[int(index % 10)] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    # notice this is done in reverse

    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


# Method to do Radix Sort

def radixSort(arr):

    # Find the maximum number in the array
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing the digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while int(max1 / exp) > 0:
        countingSort(arr, exp)
        exp *= 10


# Driver code
arr = [170, 45, 75, 9511, 9512, 24, 2, 66]

# Function Call
radixSort(arr)

for i in range(len(arr)):
    print(arr[i])
