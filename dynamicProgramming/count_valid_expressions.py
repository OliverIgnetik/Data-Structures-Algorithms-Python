"""
Count Valid Expressions
You are given an array of integers nums and an integer target.

Your goal is to build a valid expression out of nums by adding one of the symbols + and  - before each integer in nums. 
The value of this expression should be equal to target.
NOTE: you are not allow to rearrange the nums, 
all we can do is place the operators

For Example :
If nums = [3,5] you can form -
-3-5
-3+5
3-5
3+5

Return the total number of valid expressions that can be formed from the given input.

Example 1:
Input: nums =  [1,2,1] , target= 2
Output: 2
Explanation:  +1+2-1=2 and -1+2+1=2 are valid expressions

Example 2:
Input: nums =  [1,2,3] , target= 10
Output: 0
Explanation:  No Valid Expression can be made

Constraints: 

1 <= nums.length <= 20
1 <= nums[I] <= 1000
-1000 <= target <= 1000
The answer will fit in the integer range
"""


class Solution:
    def countValidExpressions(self, nums, target):
        """
        Interface
        ----
        :type nums: list of int
        :type target: int
        :rtype: int

        Approach 
        ----
        1. The problem statement clearly states that either an element can treated as positive or negative.

        2. Let 'P' be the sum of elements that need to be positive and 'N' be the sum of elements that need to be negative
                   => P-N = target 
                   => P + N + P - N = target + P + N (Adding P+N both sides in the equation)
                   => 2*P = target + sum of array 
                   => P = (target + sum of array)/2

        3. So our problem is simplified to a subset sum problem  

        Complexity
        ----
        t = target number
        n = nums we can use
        Time : O(t*n)
        Space : O(n)
        """

        num_sum = 0

        # Calculate the sum of whole array
        for i in nums:
            num_sum = num_sum + i

        # This is the corner case. Where we would not get any solution
        # NOTE: refer to proof P = (target + num_sum)/2
        if (num_sum + target) % 2 == 1 or abs(target) > num_sum:
            return 0

        # assign (sum+target)/2 to new variable
        target_sum = (num_sum + target) // 2

        # Create a DP array of size target_sum + 1 for storing values
        # NOTE: we need to include 0 as the base case
        dp = [1] + [0] * target_sum

        # Fill the DP subproblem table in a bottom up manner
        # Subproblem definition

        # NOTE: we consider unique valid expressions were we can only use
        # each of the numbers once
        for num in nums:
            for s in range(target_sum, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[target_sum]


nums = [1, 2, 1]
target = 2

s = Solution()
print(s.countValidExpressions(nums, target))
