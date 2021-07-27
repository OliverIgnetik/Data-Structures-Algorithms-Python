"""
The Change Making Problem
Given an array of integers that represent coins called coins and an integer amount amount,
return the minimum amount of coins it requires to make complete change for amount amount.

If it is not possible to make change return -1.

Example 1:
Input:
coins = [1, 2, 3]
amount = 10

Output: 4
Explanation: We can use two 3 coins & two 2 coins to fully make change for 10. 3 + 3 + 2 + 2 = 10

Example 2:
Input:
coins = [1, 3, 5, 6, 9]
amount = 90

Output: 10
Explanation: 9 x 10 uses = 90

Example 3:
Input:
coins = [2]
amount = 5

Output: -1
Explanation: We cannot make change for 5 with only a 2 coin.

Constraints:
coins[i] >= 1
Each coin will be unique
You may reuse coins
The sum of the coins used must equal amount exactly
"""

import sys


class TopDownSolution:
    def leastCoins(self, coins, amount):
        """
        Interface
        ----
        :type coins: list of int
        :type amount: int
        :rtype: int

        Approach
        ----
        1. We use a recursive approach 

        2. At each stack frame we consider what choices do we have to make
        and how does this get us to our goal

        3. What are the base cases?
        - When the remainder is less then 0 
        - When the remainder is zero

        4. The recursion tree will be very lopsided, so we see the 
        upperbound we set is very loose

        Complexity
        ----
        Time : O(amount*coins) memoization pulls us down from O(|coins|^(amount/minCoin))
        This is because the memoization saves us work
        Space : O(amount)
        """
        if amount < 1:
            return 0

        # we need to add 1 because we need a cache from 0 to amount inclusive
        # eg. 2 -> [0, 1, 2]
        return self.coin_change(coins, amount, [0] * (amount + 1))

    def coin_change(self, coins, remainder, cache):
        """
        NOTE: BASE CASE
        Minimum coins to make change for a negative amount is -1.
        This is just a base case we arbitrarily define.
        """
        if remainder < 0:
            return -1

        """
        NOTE: BASE CASE
        The minimum coins needed to make change for 0 is always 0
        coins no matter what coins we have.
        """
        if remainder == 0:
            return 0

        # We already have an answer cached. Return it.
        # NOTE: CACHING MEMOIZATION
        if cache[remainder] != 0:
            return cache[remainder]

        # No answer yet. Try each coin as the last coin in the change that we make for the amount
        system_max = sys.maxsize
        minimum = system_max
        for coin in coins:
            change_result = self.coin_change(coins, remainder - coin, cache)

            """ 
            If making change was possible (changeResult >= 0) and 
            the change result beats our present minimum, add one to
            that smallest value
          
            We accept that coin as the last coin in our change making
            sequence up to this point since it minimizes the coins we
            need
            """
            if (change_result >= 0 and change_result < minimum):
                minimum = 1 + change_result

        """
        If no answer is found (minimum == max value) then the
        sub problem answer is just arbitrarily made to be -1, otherwise
        the sub problem's answer is "minimum"
        """
        cache[remainder] = -1 if (minimum == system_max) else minimum

        return cache[remainder]


class BottomUpSolution:
    def leastCoins(self, coins, amount):
        """
        Interface
        ----
        :type coins: list of int
        :type amount: int
        :rtype: int

        Complexity
        ----
        A = maximum call stack depth (ie. we just subtract 1 at every step), 
        at each call stack we can at worst do c work
        Time : O(A*c)
        Space : O(A)
        """

        # This table will store the answer to our sub problems
        # NOTE: amount + 1 is an arbitrary place holder
        dp = [amount + 1] * (amount + 1)

        """
        The answer to making change with minimum coins for 0
        will always be 0 coins no matter what the coins we are
        given are
        """
        dp[0] = 0

        # Solve every subproblem from 1 to amount
        for i in range(1, amount + 1):
            # For each coin we are given
            for j in range(0, len(coins)):
                # If it is less than or equal to the sub problem amount
                if coins[j] <= i:
                    # Try it. See if it gives us a more optimal solution
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        """
        dp[amount] has our answer. If we do not have an answer then dp[amount]
        will be amount + 1 and hence dp[amount] > amount will be true. We then
        return -1.
  
        Otherwise, dp[amount] holds the answer
        """

        return -1 if dp[amount] > amount else dp[amount]


coins = [1, 2, 3]
amount = 10

ts = TopDownSolution()
bs = BottomUpSolution()

print(ts.leastCoins(coins, amount))
print(bs.leastCoins(coins, amount))
