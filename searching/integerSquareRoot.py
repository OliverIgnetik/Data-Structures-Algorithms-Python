"""
Compute The Integer Square Root
Given an integer n, compute the square root of n, rounded down to the nearest integer.

Example #1:
Input: 25
Output: 5
Explanation: The square root of 25 is 5.

Example #2:
Input: 8
Output: 2
Explanation: Although the square root of 8 is 2.82, we round down to the nearest integer, so the answer is 2.

Constraints:  Your solution should run in O(log(n)) time. You may not use the built-in square root function of your respective language.
"""
import math


class Solution:
    def squareRoot(self, n):
        """
        We want to find the largest integer x such that x^2 <= n.
        To do so, we can binary search the interval [1, n].

        Approach 
        ----
        1. Rephrasing the stated problem, we wish to find the 
        largest integer x such that x² is less than or equal to n.

        2. In order to find x, we can apply a binary search to the interval [0, n],
        where n is the provided integer. 

        3. We can eliminate the right half of the interval being considered if the square of the number we are currently looking
        at is greater than n.

        4. Conversely, we can update our answer variable and eliminate the left half of our interval if the square of the number 
        we are currently looking at is less than or equal to n. 

        5. The runtime of this solution is O(log(n)).

        Complexity
        ----
        Time : O(logN)
        Space : O(1)

        """
        lo = 1
        hi = n
        ans = 1

        # Perform Binary Search
        while lo <= hi:
            mid = lo + math.floor((hi - lo) / 2)

            if math.floor(mid * mid) <= n:
                # Store our best answer so far
                ans = mid
                lo = mid + 1
            else:
                # mid^2 > n, so we need to look at smaller numbers.
                hi = mid - 1

        return ans


i = 25
s = Solution()
print(s.squareRoot(25))
