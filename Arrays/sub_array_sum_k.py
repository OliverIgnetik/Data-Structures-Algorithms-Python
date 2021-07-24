"""
Given an array of integers arr and an integer value k,
return the total amount of unique, contiguous, subarrays
that sum to k in arr.

Input: [3, 7, -4, -2, 1, 5] k = 3
Output: 2
Explanation: 2 subarrays sum up to 3

                      i j
[3, 7, -4, -2, 1, 5] [0,0]
[3, 7, -4, -2, 1, 5] [1,2]
"""

from typing import List


class Solution:
    def brute_force(self, arr: List[int], k: int) -> int:
        """
        Check every subarray
        Complexity
        ----
        Time : O(N^2)
        Space : O(N^2)
        """
        seen = set()
        for i in range(len(arr)):
            sub_array_sum = 0
            sub_array = []
            for j in range(i, len(arr)):
                sub_array_sum += arr[j]
                sub_array.append(arr[j])
                if sub_array_sum == k and tuple(sub_array) not in seen:
                    seen.add(tuple(sub_array))
        return len(seen)

    def cumulative_sum(self, arr: List[int], k: int) -> int:
        """
        We can use the difference of cumulative sums. Cumulative sums
        are often helpful when dealing with subarray sums

        Complexity
        ----
        Time : O(N^2)
        Space : O(N) not including output
        """
        # Declaring a sums array for storing the sum
        sums = []
        sums.append(arr[0])
        # Storing the cumulative sum in the sums array
        for idx in range(1, len(arr)):
            sums.append(sums[idx - 1] + arr[idx])

        count = 0
        # Now we can check sub array sums by simply finding the difference between cumulative sums
        for start in range(0, len(arr)):
            for end in range(start, len(arr)):
                temp_sum = sums[end]

                # this corresponds to the sub array ranging from start to end
                if start != 0:
                    temp_sum -= sums[start - 1]

                if temp_sum == k:
                    count += 1

        return count

    def empty_gaps(self, arr: List[int], k: int) -> int:
        """
        Complexity
        ----
        Time : O(N)
        Space : O(N)
        """
        m = {}  # how many times have we seen a sum in the past?
        s = 0
        count = 0
        m[0] = 1

        for idx in range(0, len(arr)):
            # keep track of the cumulative sum
            s += arr[idx]
            """
            If we have seen (s-k) before, that means the cumulative sum of the 
            subarray between the current index and that index which yielded a 
            cumulative sum of (s-k) will be k, which is our target
            """
            if (s - k) in m:
                count += m[s - k]
            """
            We need to keep track of how many times we have seen this each cumulative 
            sum because if we have seen it more then once then there is more then one
            sub array with the target sum that we need to count
            """
            if s in m:
                m[s] += 1
            # if we have not seen this sum add once occurence to the map
            else:
                m[s] = 1
        return count


print(Solution().brute_force([3, 7, -4, -2, 1, 5], 3))
print(Solution().cumulative_sum([3, 7, -4, -2, 1, 5], 3))
print(Solution().empty_gaps([3, 7, -4, -2, 1, 5], 3))
