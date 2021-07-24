"""
Array Product
Given an array A[] of positive integers, return an array of integers whose k'th element
is equal to the product of every integer in A[] except for the k'th element in A[].

Example 1:
Input: [1, 1, 2, 5]
Output: [10, 10, 5, 2]
Explanation: 
The product of the entire array except for the first and second element is 10.
The products of the entire array except for the third and fourth elements are 5 and 2, respectively.

Constraints:  You may not use the division operation.
"""


class Solution:
    def productExceptCurrentElement(self, arr):
        """
        Interface
        ----
        :type arr: list of int
        :rtype: list of int

        Approach 
        ----
        1. Let prefix[k] represent the product of the first k elements in our provided array, and let suffix[k] represent the product of the last k elements in the provided array. 

        2. Both of these arrays can be constructed in linear time using dynamic programming. 

        3. More precisely, we use the following TWO RECURRENCES: 
        - prefix[k] = prefix[k - 1] * A[k] 
        - suffix[k] = suffix[k + 1] * A[k] 

        Letting N denote the number of elements in the provided array, our BASE CASES are:
        - prefix[0] = A[0] 
        - suffix[N - 1] = A[N - 1] 

        4.From here, we can compute the ANSWER for each entry in our array in constant time 
        the product of every element in the array except for the element at index i is: 
        - prefix[i - 1] * suffix[i + 1].

        Complexity
        ----
        Time : O(N)
        Space : O(N)
        """

        # Make a suffix and prefix array to store
        # the products of suffix and prefix elements respectively
        prefix = [1] * len(arr)
        suffix = [1] * len(arr)
        last_index = len(arr) - 1

        # Fill the prefix array
        # NOTE: this is one of the base cases
        prefix[0] = arr[0]
        for i in range(1, len(arr)):
            prefix[i] = prefix[i - 1] * arr[i]

        # Fill the suffix array
        # NOTE: this is one of the base cases
        suffix[last_index] = arr[last_index]
        for i in range(last_index - 1, -1, -1):
            suffix[i] = suffix[i + 1] * arr[i]

        ans = [1] * len(arr)

        # The value of ith element is multiplication of its prefix and suffix
        for i in range(0, len(arr)):

            # Multiply prefix except for first element
            # NOTE: it doesn't make sense to ask the prefix of the first index
            if i != 0:
                ans[i] *= prefix[i - 1]

            #  Multiply suffix except for last element
            # NOTE: it doesn't make sense to ask the suffix of the last index
            if i != last_index:
                ans[i] *= suffix[i + 1]

        return ans


arr = [1, 1, 2, 5]
s = Solution()
print(s.productExceptCurrentElement(arr))
