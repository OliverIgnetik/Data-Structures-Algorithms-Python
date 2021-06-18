# naive solution
from nose.tools import assert_equal
import collections

################ Problem Definition ###########################
"""
Consider an array of non-negative integers. A second array is formed by
shuffling the elements of the first array and deleting a random element.
Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is
removed to construct the second array.

Input:

    finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:

    5 is the missing number

"""
################ Solution #####################################

# naive solution


def finder(arr1, arr2):

    # Overall time complexity -> 2NlogN + N -> O(NlogN)
    # Sort the arrays
    arr1.sort()  # NlogN
    arr2.sort()  # NlogN

    # Compare elements in the sorted arrays
    for num1, num2 in zip(arr1, arr2):  # N
        if num1 != num2:
            return num1

    # Otherwise no elements have been deleted
    print('Elements are common in both arrays')
    return


# O(N) solution

def finder2(arr1, arr2):

    # Using default dict to avoid key errors
    # initialize a dictionary with 0
    d = collections.defaultdict(int)

    # linear time -> 2N+1 -> O(N) time complexity
    # Add a count for every instance in Array 2
    for num in arr2:
        d[num] += 1

    # Check if num not in dictionary
    # check arr1 after because the number is removed in arr2
    for num in arr1:
        if d[num] == 0:
            return num
        # Otherwise, subtract a count
        else:
            d[num] -= 1


# XOR solution

def finder3(arr1, arr2):
    result = 0

    # Perform an XOR between the numbers in the arrays
    # XOR is good for pairs
    for num in arr1 + arr2:  # O(N) time complexity
        result ^= num

    return result


class TestFinder(object):

    def test(self, sol):
        assert_equal(sol([5, 5, 7, 7], [5, 7, 7]), 5)
        assert_equal(sol([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        assert_equal(sol([9, 8, 7, 6, 5, 4, 3, 2, 1],
                         [9, 8, 7, 5, 4, 3, 2, 1]), 6)
        print('ALL TEST CASES PASSED')


arr1 = [5, 5, 7, 7]
arr2 = [5, 5, 7, 7]
print(finder(arr1, arr2))

# t = TestFinder()
# t.test(finder3)
