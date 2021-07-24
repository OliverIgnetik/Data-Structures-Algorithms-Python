"""
Erase Interval Overlaps
Given a sequence of intervals return the minimum amount of intervals that need to be erased to eliminate all overlap conflicts.

Intervals i and j overlap if any of the following hold:
start(i) < start(j) and end(i) > start(j)
start(j) < start(i) and end(j) > start(i)
start(i) = start(j)

Example 1:
Input:
[
  [1, 2],
  [2, 3],
  [3, 4],
]
Output: 0
Explanation: No intervals removed, no overlaps.

Example 2:
Input:
[
  [1, 2],
  [1, 2]
]
Output: 1
Explanation: The minimum amount of intervals that need to be removed to make a non-overlapping set of intervals is 1, the [1, 2] interval.

Constraints:
1 <= start(i) < end(i) <= 100
Starts and ends of intervals will be integers
You must maintain the relative ordering of the intervals as they stood in the original interval sequence
"""


class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        Interface 
        ----
        :type intervals: list of list of int
        :rtype: int

        Approach 
        ---- 
        1. We need to generate the maximum non-overlapping set of intervals
        2. Make use of greedy algorithm to choose the locally best solution to find the global optimum
        NOTE: that choice is never reconsidered later in the problem
        3. First we need to sort the intervals by their finish time
        4. We add intervals that have a start time greater than or equal to the currently considered interval 
        5. When we add the new interval we have to update the end of the active interval
        6. Find the difference between the total number of intervals and the maximum non-overlapping set

        Complexity
        ----
        Time : O(NlogN) due to initial sort
        Space : O(1) Not including output
        """

        # If the size of intervals is 0, Return 0
        if len(intervals) == 0:
            return 0

        # Sort on the end
        def interval_cmp(a):
            return a[1]

        # Sort the intervals vector according to the increasing
        # Order of their end time
        intervals.sort(key=interval_cmp)

        # It stores the current end time of iterval
        end_of_active_interval = intervals[0][1]

        # It stores the total intervals
        total_intervals_in_nonoverlapping_set = 1

        for interval in intervals:
            interval_start = interval[0]
            interval_end = interval[1]

            # Case when new interval is to be formed
            # NOTE: we can only add a new interval when the start is greater
            # than or equal to the end of the currently considered interval
            if interval_start >= end_of_active_interval:
                end_of_active_interval = interval_end
                total_intervals_in_nonoverlapping_set += 1

        # Return the number of intervals needed to be erased
        return len(intervals) - total_intervals_in_nonoverlapping_set


intervals = [
    [1, 2],
    [2, 3],
    [3, 4],
]

s = Solution()
num_removed = s.eraseOverlapIntervals(intervals)
print(num_removed)
