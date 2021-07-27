"""
Intersection of 2 Sorted Arrays
Given two sorted arrays, return a new array that represents their intersection. 

Example 1:
Input:
[1,2,3,5] 
[1,2] 

Output: 
[1,2]

Example 2:
Input:
[1,2,2,3]
[1,1,4]

Output: 
[1]

Constraints
Each element in the result must be unique.
"""


class LinearSolution:
    def intersection(self, nums1, nums2):
        """
        Interface
        ----
        :type nums1: list of int
        :type nums2: list of int
        :rtype: list of int

        Approaches
        ----
        1. Use a binary search because the items are sorted in both arrays 

        2.  We can do a two pointer scan which improves the time complexity to pseudo linear time

        3. Alternatively we could put one array in a set so we would get:
        Time : O(m + n)
        Space : O(max(m, n))

        Complexity
        ----
        Time : O(m + n)
        Space : O(1)
        """

        # Create a Set for storing the elements which are common
        intersection = set()

        ptr1 = 0
        ptr2 = 0
        # Iterate all the elemnts of both the array
        while (ptr1 < len(nums1) and ptr2 < len(nums2)):

            # If the elements are same, Add it to the set
            # And Increment both the pointers
            if nums1[ptr1] == nums2[ptr2]:
                intersection.add(nums1[ptr1])
                # we consumed both items so increment both pointers
                ptr1 += 1
                ptr2 += 1
            # If element of first array is less than element of second array increment ptr1
            elif nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            # Else increment ptr2
            else:
                ptr2 += 1
        # Return the ans after converting it to array
        return list(intersection)


class BinarySearchSolution:
    def intersection(self, nums1, nums2):
        """
        Interface
        ----
        :type nums1: list of int
        :type nums2: list of int
        :rtype: list of int

        Complexity
        ----
        Time : O(min(m,n)*log(max(m,n)))
        Space : O(1)
        """
        # Set is used to eliminate duplicates
        intersection = set()
        # Iterate over the first array and search if any of its elements are present in second using Binary Search
        for i in range(0, len(nums1)):
            if i == 0 or nums1[i] != nums1[i - 1]:
                found = self.binary_search(nums2, nums1[i])

                if found:
                    intersection.add(nums1[i])

        # Return the ans after converting set to list
        return list(intersection)

    # Helper Function for performing binary search
    def binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)

            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False


m = [1, 2, 3, 5]
n = [1, 2]
s = LinearSolution()
s.intersection(m, n)
