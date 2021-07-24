"""
Longest Non-Decreasing Subsequence
Given an array on integers return the length of the longest non-decreasing subsequence.

A "subsequence" of a sequence is a subset of the sequence's elements where the original ordering of the elements is maintained. 
NOTE: A subsequence does not have to be contiguous but can be.

A "non-decreasing subsequence" is a subsequence whose values either stay the same or increase as the sequence progresses in natural order (does not decrease).

Example 1:
Input: [1,2,3,4,5,6]
Output: 6
Input: The LNDS goes from index 0 to index 5 (contains 6 elements).

Example 2:
Input: [20,30,30,20,19,90]
Output: 4
Input: The LNDS contains elements at index 0, 1, 2, & 5 (4 elements).
"""


class Solution:
    def lengthOfLNDS(self, nums):
        """
        Interface
        ----
        :type nums: list of int
        :rtype: int

        Approach 
        ----
        1. Identify subproblems and cache subproblem answers

        2. Establish base cases

        3. We treat every item in the array as the last item in 
        a longest increasing subsequence 

        4. Each cache entry is the best answer for the longest increasing 
        subsequence that ends at that index

        Complexity
        ---- 
        Time : T(N) is O(N^2) 
        T(N) = N(N-1)/2 = 1 + 2 + 3 + 4 + ... + (N-1)

        Space : O(N)
        """

        # Case when input array is empty
        if not nums:
            return 0

        max_length = [1] * len(nums)

        # By default the best answer is a length of 1
        maximum_so_far = 1

        # Test every possible end index of a longest increasing subsequence
        # i constitute to the ending index of the subsequence
        for i in range(1, len(nums)):

            # Check for all the indices before i
            # j will constitute to the second last index of subsequence
            for j in range(0, i):

                # If jth element can be the next element
                # That is nums[i] >= nums[j]
                if nums[i] >= nums[j]:
                    # Update the ans of index i
                    max_length[i] = max(max_length[i], max_length[j] + 1)

            # Update the maximum length till index i
            maximum_so_far = max(maximum_so_far, max_length[i])

        return maximum_so_far


# NOTE: remember the longest non decreasing subsequence does not have to contiguous
arr = [1, 2, 3, 4, 5, 6]
s = Solution()
res = s.lengthOfLNDS(arr)
print(res)
