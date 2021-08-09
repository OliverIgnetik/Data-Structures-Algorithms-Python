"""
Buy and Sell Stock Once
We are given an array arr where the i'th element is the price for a stock on day i.

Determine the maximum profit that can be yielded by buying and selling a stock once.

Example 1:
Input: [1,2,3,4,5,6]
Output: 5
Explanation: You buy on day 0 and sell on day 5 for a profit of 6 - 1 = 5.

Example 2:
Input: [12,4,6,9,3,8,4]
Output: 5
Explanation:
Two ways to achieve max profit:
1.) Buy on day 1 and sell on day 3 for a profit of 9 - 4 = 5
2.) Buy on day 4 and sell on day 5 for a profit of 8 - 3 = 5

Constraints:
You may not buy and sell a stock on the same day
"""


class LinearSpaceSolution:
    def maxProfit(self, prices):
        """
        Interface
        ----
        :type prices: list of int
        :rtype: int

        Approach
        ----
        1. Use dynamic programming and look at subproblems
        2. We can choose:
        - extend the profit : p[i] - p[i-1] + opt[i-1]
        where opt[i-1] is the optimal solution for the (i-1)th day
        OR 
        - buy and sell on the same day : 0 

        Complexity
        ----
        Time : O(N)
        Space : O(N)
        """

        # Case when number of days = 0
        if not prices:
            return 0

        # It tell us the best price we can get if we sell at day i
        opt = [0] * len(prices)

        # It tells us the maximum total after n days
        global_max = 0

        # Traverse the array from day 2
        for i in range(1, len(prices)):

            # Take the difference between adjacent prices
            profit_delta = prices[i] - prices[i - 1]

            # If total profit at ith day is > 0 store it
            # Otherwise store 0 ie. buy and sell on the same day
            opt[i] = max(0, opt[i - 1] + profit_delta)

            # Calculate global Max by comparing all the opt[i] value
            global_max = max(global_max, opt[i])

        return global_max


class ConstantSpaceSolution:
    def maxProfit(self, prices):
        """
        Interface
        ----
        :type prices: list of int
        :rtype: int

        Approach
        ----
        1. Use Kadane's algorithm 
        2. It's helpful to graph this as we can clearly identify the most
        important feature is the minimum and maximum

        Complexity
        ----
        Time : O(N)
        Space : O(1)
        """

        # Case when prices array is empty
        if not prices:
            return 0

        # Only 1 thing matters: lowest price seen so far, 'globalMin'

        # Global Max will contain the maximum Profit so far
        global_max = 0

        # GlobalMin will contain the minimum value of stock so far
        global_min = prices[0]

        # Traverse The array from day 1
        for price in prices:

            # Store the global minimum
            global_min = min(global_min, price)

            # Calculate the profit by subtracting the price at day i with global minimum
            # NOTE: subproblems are hidden
            # You can see the nature of the subproblems in the linear space solution
            global_max = max(global_max, price - global_min)

        return global_max


stock_values = [1, 2, 3, 4, 5, 6]

sL = LinearSpaceSolution()
sC = ConstantSpaceSolution()

print(sL.maxProfit(stock_values))
print(sC.maxProfit(stock_values))
