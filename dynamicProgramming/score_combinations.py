"""
Score Combinations
Given an array scoreEvents of possible score point amounts in a sports match and an integer amount finalScore (the final score of the game), return the total of possible unique score event arrangements that would result in the value of finalScore.

Example 1:
Input:
scoreEvents = [2,3,7]
finalScore = 12

Output: 4
Explanation:
There are 4 possible ways that the game ended with a final score of 12:
1.) [2, 2, 2, 2, 2, 2]
2.) [3, 3, 3, 3]
3.) [2, 2, 2, 3, 3]
4.) [2, 3, 7]

Example 2:
Input:
scoreEvents = [2,4,5]
finalScore = 9

Output: 2
Explanation:
There are 2 possible ways that the game ended with a final score of 9:
1.) [2, 2, 5]
2.) [4, 5]

Example 2:
Input:
scoreEvents = [4,5]
finalScore = 11

Output: 0
"""


class Solution:
    def totalWaysToReachScore(self, finalScore, pointEvents):
        """
        Interface
        ----
        :type finalScore: int
        :type pointEvents: list of int
        :rtype: int

        Approach
        ----
        Recursive Approach
        e = point events
        me = min point event
        s = total score

        We could have a function with a signature like:
        func(score, pointEvents, path, set)

        This kind of approach might have a recursion tree with a depth bounded:
        O(s/me))
        NOTE: if me = 1 then O(s)

        And the overall algorithm will have a runtime bounded by:

        O(e^s/me)

        Dynamic Programming Approach
        NOTE: Tip for dynamic programming problems, consider if there is a yes/ no question
        1. Make use of 2D cache to record subproblem answers. We need to keep 
        track of uniqueness aswell

        2. Identify binary choice. Do we include the point event?
        yes : how many ways can we construct the score using the remaining point events 
        containing this point event in question?
        - if yes then stay in the same row
        no : how many ways can we construct the score using the remaining point events?
        - if no then go up a row

        3. Record how many unique ways there are to reach each score 

        4. Identify the base cases 
        - we have no pointEvents to make the score with
        - we have a score of 0

        5. Also we have to make sure the pointEvents we consider are less then the score
        Complexities
        ----
        s = total score
        e = point events

        Time : O(s*e)
        Space : O(s*e)

        Assumptions
        ----
        We assume pointEvents is sorted
        """

        # The row indicates considering the row'th item for use. The column
        # indicates the score amount to determine total combinations for.
        ways_cache = [[0] * (finalScore + 1)] * (len(pointEvents) + 1)

        # There is 1 way to reach score 0 given any amount of items, to not score at all
        for row in range(1, len(pointEvents) + 1):
            ways_cache[row][0] = 1

        # we start here implying the first row is our base case
        for row in range(1, len(pointEvents) + 1):
            for score in range(1, finalScore + 1):
                event_value = pointEvents[row - 1]

                # Don't use this event value, the 'totalScore' to "make change" remains intact
                # NOTE: go up one row, ie. we have one less pointEvent to choose from
                without_this_event = ways_cache[row - 1][score]

                # We use this event value, we can continue to use it so we don't go up a row,
                # the 'totalScore' to "make change" decreases
                with_this_event = 0
                # we can only use event values less then or equal to the current score
                if event_value <= score:
                    with_this_event = ways_cache[row][score - event_value]

                # we update the cache with the sum o
                ways_cache[row][score] = without_this_event + with_this_event

        # we return the bottom right corner of the matrix
        return ways_cache[len(pointEvents)][finalScore]


# we assume scoreEvents is sorted
scoreEvents = [2, 3, 7]
finalScore = 12
s = Solution()
s.totalWaysToReachScore(finalScore, scoreEvents)
