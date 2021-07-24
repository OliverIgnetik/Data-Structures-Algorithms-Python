"""
Maximum Total Points
You are given n balls indexed from 0 to n-1. Each ball has a value associated with it represented by an array nums. You are asked to remove each ball one by one until all the balls are removed.


If you remove the ith ball, you will get (nums[i-1] * nums[i] * nums[i+1]) points. If i-1 or i+1 goes out of bounds of the array then treat it as if there is a ball with a value 1 associated with it.


Return the Maximum total points you can obtain by removing the balls wisely.


Example 1:
Input: [3,5,8]
Output: 152
Explanation:  
nums =  [3,5,8] → [3,8] →  [8]  → []
points = 3*5*8  + 1*3*8 + 1*8*1 = 152

Constraints: 

1 <= nums[I] <=100
1 <= n <= 100
The answer will fit in the integer range
"""


class Solution:
    def maxPoints(self, nums):
        """
        Interface
        ----
        :type nums: list of int
        :rtype: int

        Complexity
        ----
        Time : O(N^3) 

        Approach
        ----
        DP[I][j] is the maximum points we can get from i to j. 
        NOTE: - when i > j, then DP[I][j]=0

        """
        # Insert 1 at the begining and end of the nums vector
        # It is added to handle the corner cases
        nums = [1] + nums + [1]
        N = len(nums)
        DP = [[0] * N for _ in range(N)]
        # build up the solution in a bottom up manner
        for gap in range(2, N):
            for i in range(N - gap):
                # dp[i][j] = the maximum points we get after removing all balls between
                # i and j (excluding i and j themselves)
                j = i + gap
                for k in range(i + 1, j):
                    DP[i][j] = max(DP[i][j], nums[i] * nums[k]
                                   * nums[j] + DP[i][k] + DP[k][j])
                    # maximum points of removing all the balls on the left side of i
                    # maximum points of removing all the balls the right side of i
                    # removing ball i last when left side and right side are gone
        return DP[0][N - 1]


nums = [3, 5, 8]
s = Solution()
print(s.maxPoints(nums))
