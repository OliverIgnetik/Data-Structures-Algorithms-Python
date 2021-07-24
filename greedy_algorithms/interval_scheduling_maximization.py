"""
Interval Scheduling Maximization
Given a set of intervals intervals, return a maximal set of the intervals that has no overlaps.

Two intervals overlap if one interval's end strictly crosses another interval's start time.

Example 1:
Input:
[
  [0, 3],
  [0, 6]
]

Output:
[
  [0, 3]
]

Explanation: The two intervals overlap so either could be removed to yield a valid solution. The most intervals that can be preserved is 1.

Example 2:
Input:
[
  [0, 3],
  [0, 6],
  [0, 17],
  [8, 11],
  [19, 23]
]

Output:
[
  [0, 3],
  [8, 11],
  [19, 23]
]

Explanation: Since we choose to keep [0, 3] we cannot keep [0, 6] and [0, 17] since they overlap. The rest of the provided intervals do not overlap.

Constraints:
0 < start(i) < end(i)
start(i) and end(i) will always be integers
"""

import sys


class Solution:
    def constructOptimalSchedule(self, intervals):
        """
        Interface 
        ----
        :type intervals: list of list of int
        :rtype: list of list of int

        Approach
        ----
        1. This is a scheduling problem. These types of a problems are great for greedy algorithms 
        2. We need to return a maximal set of intervals with no overlaps
        3. This set will be the optimal schedule

        Proof
        ----
        NOTE: We know that the cardinality of the optimum solution (|O|) will satisfy:
        |O| >= |G|
        Where |G| is the cardinality of the greedy solution

        If we can prove the |O| = |G| thus the greedy solution is the optimal solution
        We make use of an exchange arguement and slowly transform the greedy solution into the optimum solution

        Complexity
        ----
        Time : O(NlogN)
        Space : O(1) Not including the outpu
        """
        # Create a 2D Array for storing the answer
        optimal_schedule = []

        def interval_cmp(a):
            return a[1]

        # Sort the intervals vector according to the increasing
        # Order of their end time
        intervals.sort(key=interval_cmp)

        # It contains the end time of current interval
        last_scheduled_interval_finish = -sys.maxsize - 1

        # Iterate through all the intervals
        for interval in intervals:
            start = interval[0]

            # Case when new interval is to formed
            if start >= last_scheduled_interval_finish:
                end = interval[1]

                optimal_schedule.append(interval)
                last_scheduled_interval_finish = end

        return optimal_schedule


schedule = [
    [0, 3],
    [0, 6],
    [0, 17],
    [8, 11],
    [19, 23]
]

s = Solution()
optimal_schedule = s.constructOptimalSchedule(schedule)
print(optimal_schedule)
