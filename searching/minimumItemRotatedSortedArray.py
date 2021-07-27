"""
Minimum Item In A Rotated Sorted Array
Given a rotated sorted array, find the minimum element.

A "rotated" array is an array that has had each item shifted to
the left or right by k units (where k is a positive integer) while maintaining
positional integrity of every element in the original array.

Example 1:
Input: [4, 5, 6, 7, 1, 2]
Output: 1

Example 2:
Input: []
Output: -1

Example 3:
Input: [55, 88, 91, 93, 2, 9, 20]
Output: 2

Follow-Up:
Can you do this in O(log(n)) time?

Constraints:
arr[i] >= 0
All Elements in the array are unique
"""


class Solution:
    def findMin(self, nums):
        """
        Interface 
        ----
        :type nums: list of int
        :rtype: int

        Approach
        ----
        1. Use a modified binary search 

        2. We know the array is sorted even though it is shifted it
        would be unnecessary to look at all the items

        Complexity
        ----
        Time : O(logN)
        Space : O(1)

        """
        # Make a left pointer and right pointer for performing binary search
        # Inititalize left=0 and right = size-1 as lower and upper bounds
        left = 0
        right = len(nums) - 1

        # Perform Binary Search
        while left < right:

            # Take the middle value.
            # NOTE: This method is preferred for taking the middle to avoid integer overflow
            mid = left + ((right - left) // 2)

            # NOTE: this is where we modify binary search
            # If mid element is greater than right element then update left
            # the drop and hence the minimum item is in the right hand portion

            if nums[mid] > nums[right]:
                left = mid + 1

            # the minimum item is in the left hand portion
            else:  # Else update right
                right = mid

        # Return the element at the left index
        return nums[left] if len(nums) > 0 else -1


i = [4, 5, 6, 7, 1, 2]
s = Solution()
print(s.findMin(i))
