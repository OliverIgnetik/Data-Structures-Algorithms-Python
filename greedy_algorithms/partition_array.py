"""
Partition Array
Given an array of integers A[] and an integer k, return true if it's possible to partition A[] into sets of k consecutive integers. 

Example 1:
Input: A = [1, 3, 2, 3, 4, 5], k = 3
Output: true
Explanation We can partition our array into the two subarrays [1, 2, 3] and [3, 4, 5]. Both of these subarrays consist of three consecutive integers.

Example 2:
Input: A = [1, 3, 2, 2, 1], k = 3
Output: false
Explanation There is no way to partition our array into groups of three consecutive integers.
"""

import collections


class Solution:
    def canPartition(self, arr, k):
        """
        Interface
        ----
        :type arr: list of int
        :type k: int
        :rtype: bool

        Approach
        ----
        1. The key observation is that every element in the array either starts a new "run"
        of k consecutive integers, or it continues a previously started run. 

        2. The approach is to keep a sorted map to store the number of times that each number occurs in the original array.

        3. Subsequently, we can iterate over the elements in the array in ascending order.

        4. While processing the values, we keep an integer value called "last_checked" to represent the previous value that 
        we just processed (since we need to make sure that our runs consist of consecutive integers).

        5. Furthermore, we keep another integer variable called "ongoing_runs" to keep track of the number of runs of length k
        that are in the process of being constructed.

        6. Finally, we keep a queue to keep track of the number of runs starting at each value. 
        This queue is maintained as we process each value. As we process each value, we make sure that the number of occurrences
        of the value is enough to extend all of the ongoing runs. 

        7. Furthermore, we verify that if we have any ongoing runs, then our values are consecutive. 
        If either of these conditions do not hold, we immediately stop processing and return false. 
        If we are able to successfully process every value, then we return true. 

        Complexity
        ----
        The runtime of this algorithm is O(Nlog(|N|) + N), where N is the number of elements in the inputted array. 
        This follows from the fact that we perform exactly N increment operations in our ordered map (which is typically implemented as a balanced binary tree).
        Each of these N operations requires O(log(|N|)) time since our data structure will contain at most |N| elements. 
        Finally, we must account for the fact that we are iterating over N elements, and this process itself may take longer than the insertions. 
        Thus, we add a factor of N to our analysis.

        Time : O(Nlog(|N|) + N)
        Space : O(|N|)
        """
        # Record the frequency of each number in a mapping
        # NOTE: we can assume radix sort here ie. O(N+k)
        arr = sorted(arr)
        # OrderedDict is useful here because we want to keep track of insertion order
        frequency = collections.OrderedDict()
        for item in arr:
            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1

        starts = []  # Keep track of the number of runs starting at each value
        last_value = -1  # Track the last value we processed
        ongoing_runs = 0  # Track of the number of runs of length k in progress
        for value, occurrences in frequency.items():
            if ongoing_runs > 0 and value > last_value + 1:
                """
                We have an ongoing run, and we skipped an integer.
                This is not allowed -- we need consecutive numbers.
                """
                return False

            if ongoing_runs > occurrences:
                """
                We don't have enough occurrences of the current value 
                to fulfill all of our ongoing runs.
                """
                return False

            """
            Everything is good to proceed.
            'occurrences - ongoingRuns' counts the # of runs newly
            starting at this value 'value'
            """
            starts.append(occurrences - ongoing_runs)
            last_value = value
            ongoing_runs = occurrences

            if len(starts) == k:
                # We just finished at least one run
                ongoing_runs -= starts.pop(0)

        return ongoing_runs == 0


A, k = [1, 3, 2, 3, 4, 5], 3

s = Solution()
partition_bool = s.canPartition(A, k)
print(partition_bool)
