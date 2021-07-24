"""
Minimum Steps to Reach 1
Given a positive integer n, return the minimum number of operations needed to reduce n to 1 using the following procedure:

Rule 1.) If the current value of n is odd, you must subtract one from n. 
Formally, if n is odd, then the new value of n becomes n-1, and the number of operations increases by one.

Rule 2.) Conversely, if the value of n is even, then you have the option to divide n by two or subtract one from n. 
Formally, if n is even, then you have the option of setting n to n/2 or n-1. In either case, the number of operations increases by one.

Example #1:
Input: 17
Output: 5
Explanation: The number 17 can be reduced to 1 in five steps as follows: 17 -> 16 -> 8 -> 4 -> 2 -> 1. No quicker solution exists.

We used:
1.) Rule 1
2.) Rule 2 (division by 2)
3.) Rule 2 (division by 2)
4.) Rule 2 (division by 2)
5.) Rule 2 (either division by 2 or subtraction by 1)

Example #2:
Input: 7
Output: 4
Explanation: The number 7 can be reduced to 1 in four steps as follows: 7 -> 6 -> 3 -> 2 -> 1. No quicker solution exists.

We used:
1.) Rule 1
2.) Rule 2 (division by 2)
3.) Rule 1
4.) Rule 2 (either division by 2 or subtraction by 1)
"""


class Solution:
    def minimumStepsToReachOne(self, input):
        """
        Interface
        ----
        :type input: int
        :rtype: int

        Approach 
        ----
        1. First check
        - If input is odd we have to subtract by 2 and the divide by 2 : 2 operations
        NOTE: input & 1 will return 1 if the number is odd
        - If input is even we have to divide by 2 : 1 operations
        2. Right shift (equivalent to dividing by 2)
        - NOTE: this is equivalent to dividing by 2

        3. Continue until we reach 1

        Complexity
        ----
        Time : O(1)
        Space : O(1)
        """

        # Case when input is already 1
        if input == 1:
            return 0

        # It will count the number of operations
        operations = 0

        # Loop till input is greater than 0
        while input != 0:

            # if input is odd add 2 to operations
            # else if input is even add 1 to operations
            operations += (input & 1) + 1

            # Right shift of input
            # It is equivalent to dividing the number by 2
            input >>= 1

        # We substract 2 because we have calculated the ans till it has become 0
        # So we reduce the number of steps required to convert from 1 to 0 i.e - 2
        return operations - 2


s = Solution()
print(s.minimumStepsToReachOne(14))
