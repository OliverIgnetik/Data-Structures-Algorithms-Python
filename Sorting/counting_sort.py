# Simple snippets explanation : https://www.youtube.com/watch?v=Rl2Ok_H-Qms&t=4s

def solution(unsorted_prices, max_price):

    # list of 0s at indices 0 to max_price
    prices_to_counts = [0] * (max_price + 1)

    # populate prices
    for price in unsorted_prices:
        prices_to_counts[price] += 1

    # populate final sorted prices
    sorted_prices = []
    # For each price in prices_to_counts
    for price, count in enumerate(prices_to_counts):
        # for the number of times the element occurs
        for _ in range(count):
            # add it to the sorted price list
            sorted_prices.append(price)

    return sorted_prices


print(solution([2, 2, 2, 7, 3, 2, 9], 10))


#######################################################
# ALTERNATIVE SOLUTION
#######################################################
# Python program for counting sort

# The main function that sorts the given string arr[] in
# alphabetical order


def countSort(arr):

    # The output character array that will have sorted arr
    output = [0 for i in range(len(arr))]

    # Create a count array to store count of individual
    # characters and initialize count array as 0
    count = [0 for i in range(256)]

    # Store count of each character
    for i in arr:
        count[ord(i)] += 1

    # Change count[i] so that it contains the actual
    # position of each character in output array
    for i in range(256):
        count[i] += count[i-1]

    # Build the output character array
    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1

    return output


# Driver program to test above function
arr = "geeksforgeeks"
ans = countSort(arr)
print("Sorted character array is % s" % ("".join(ans)))

# This code is contributed by Nikhil Kumar Singh
