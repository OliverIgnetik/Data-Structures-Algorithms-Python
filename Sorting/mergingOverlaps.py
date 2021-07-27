"""
Merge Overlapping Intervals
Given a list of intervals A, return a new list with each overlapping intervals merged.

Note On Equivalent Boundaries: If an end-point and start-point of 2 intervals are equivalent (ex: [10, 11], [11, 12]) then the intervals also overlap.

Example #1:
Input: [[1, 4], [1, 5]]

|--|--|--|--|--|--|--|--|--|--|--|--|--|--|

x========x
x===========x

Output: [1, 5]

|--|--|--|--|--|--|--|--|--|--|--|--|--|--|

x===========x

Explanation: The intervals [1, 4] and [1, 5] are overlapping, so they are merged to a single interval.

Example #2:
Input: [[1, 5], [2, 3], [4, 10], [13, 15]]

|--|--|--|--|--|--|--|--|--|--|--|--|--|--|

x===========x
   x==x
         x=================x
                                    x=====x

Output: [[1, 10], [13, 15]]
Explanation: The first three intervals are merged into a single interval. The last interval cannot be merged since it is disjoint from the other intervals.

Constraints:
For any i'th interval, A[i][0] >= 1 and A[i][1] >= 1
For any i'th interval, A[i][1] >= A[i][0]
"""


class Solution:
    def mergeOverlappingIntervals(self, A):
        """
        Interface
        ----
        :type A: list of list of int
        :rtype: list of list of int

        Complexity
        ----
        Time : O(N+k) assuming radix sort
        Space : O(1) not including the output
        """
        # If there are less than two intervals, we cannot merge anything.
        if len(A) <= 1:
            return A

        #  Sort our intervals in non-descending order by start time
        def interval_cmp(a):
            return a[0]
        # NOTE: we can assume that this is radix sort -> O(N+k)
        A.sort(key=interval_cmp)

        # merged_intervals will store our final intervals
        merged_intervals = []

        # current_interval represents the current interval being constructed.
        current_interval = A[0]
        for interval in A:
            start = interval[0]
            end = interval[1]

            if start <= current_interval[1]:
                # The current interval we are constructing overlaps with the next interval.
                current_interval[1] = max(current_interval[1], end)
            else:
                # The next interval is disjoint from the current interval being constructed.
                merged_intervals.append(current_interval)
                # update the current_interval as we found a disjoint interval
                current_interval = [start, end]

        merged_intervals.append(current_interval)

        return merged_intervals


arr = [[1, 5], [2, 3], [4, 10], [13, 15]]
s = Solution()
print(s.mergeOverlappingIntervals(arr))
