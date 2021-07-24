"""
Maximum Sum in a Circular Array
Given a "circular array" nums containing integers, return the sum of the subarray with the largest sum.

A subarray is an array within another array. Unlike subsequences, they are contiguous meaning that there are no "gaps" in the subarray taken from the overarching array.

Here, we define a circular array to be an array whose start is connected to its end.

Example:
Input: [20, -100, 20]
Output: 40
Explanation: We can take the subarray [20, 20] whose sum is 20 + 20 = 40. Note that this is possible since our array is circular and we can loop around the back (index 2 to index 0).
"""


class Solution:
    def maxCircularSubarraySum(self, nums):
        """
        Interface
        ----
        :type nums: list of int
        :rtype: int

        Approach
        ----
        Use Kadane's algorithm 

        1. There are two collectively exhaustive cases together: 
            a) Our maximum sum subarray can either consist of only contiguous elements in our original array 
            b) Or it can "wrap around" the end of the subarray We can compute the maximum sum of a subarray under both of these conditions, 
            and the maximum of the two values we find will be our overall answer. 
            NOTE: we need hold a subproblem competition

        2. First of all, we can compute the maximum sum of a circular subarray by using Kadane's algorithm. This is discussed in the solution to the
        problem "Max Contiguous Subarray Sum" (if you need a refresher view that first).

        3. The only other case to consider is when our subarray wraps around the end of our original array. 

        4. However, the maximum sum in a circular subarray is simply : 
        the sum of the entire array minus the sum of a minimum sum contiguous subarray (which can potentially be empty). 

        5. By subtracting the minimum sum contiguous subarray, we are essentially "excluding" this portion from what we are taking to form a circular subarray.
        NOTE: The reason why we exclude the minimum subarray to form a maximum circular subarray is because we are required to remove something, so it is optimal to 
        remove the part of our array that contributes the least (or a negative amount) to our sum. 

        6. For example, the minimum contiguous subarray in the array [20, -100, 20] is -100. Thus, the maximum sum circular subarray is the sum of the entire array 
        (which is 20 + -100 + 20 = -60) minus the sum of the minimum contiguous subarray. This leads us to an answer of -60 - (-100) = 40. 

        7. The minimum contiguous subarray sum can be found by negating the elements of the original array, applying Kadane's algorithm to find the maximum contiguous subarray sum,
        and finally negating the final answer. 
        NOTE: There is one special case: our minimum subarray cannot include every element in the array because, otherwise, our array would be empty.

        Complexity
        ----
        Time : O(N)
        Space : O(1)
        """

        # First, we compute the max contiguous sum and total sum.
        max_sum = nums[0]
        total_sum = 0
        curr_sum = 0
        for i in range(0, len(nums)):
            value = nums[i]
            # reset the maximum contiguous sum if we have sum less then zero
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += value
            total_sum += value
            max_sum = max(max_sum, curr_sum)

            # Negate elements in the array to find minimum contiguous sum next.
            nums[i] = -value

        # Next, we find the minimum contiguous sum.
        # NOTE: we run kadane's algorithm on an array with every element negated
        min_sum = nums[0]
        curr_sum = 0
        for value in nums:
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += value
            min_sum = max(min_sum, curr_sum)
        # the min_sum will be the negation
        min_sum = -min_sum

        # Now, we return the best of our two cases.
        return max(total_sum - min_sum, max_sum)


arr = [20, -100, 20]
s = Solution()
print(s.maxCircularSubarraySum(arr))
