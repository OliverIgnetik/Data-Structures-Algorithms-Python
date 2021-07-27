"""
4 Sum
You are given four integer arrays , nums1 , nums2 , nums3 ,  nums4 . 
All the arrays are of equal length ( say n ). Your task is to return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4 [l] == 0

Example 1:
Input:
[3,2,1] 
[4,-1,-2] 
[-1,2,-4]
[2,0,3]

Output: 6


Constraints
nums1.length == nums2.length == nums3.length == nums4.length
1 <= Size Of Array <= 100
-10000 <= array elements <= 10000
The ans will fit in the Integer range
"""


class HashMapSolution:
    def Four_Sum(self, nums1, nums2, nums3, nums4):
        """"
        Interface
        ----
        :type nums1: list of int
        :type nums2: list of int
        :type nums3: list of int
        :type nums4: list of int
        :rtype: int

        Approach 
        ----
        1. In this Approach, First we store all possible sum that can be formed using 1 element from nums1 and 1 element from nums2 in a HashMap along with its frequency. 

        2. After that for each possible combination of nums3[k]+ nums4[l], 

        3. We check the frequencies of their additive inverse that exists in the map and add it to the answer. 

        Complexity
        ---- 
        Time : O(N*N)
        Space : O(N*N)
        """

        # Create a Hash Table for storing sum of first two arrays
        hashtable = {}

        # Traverse the first two arrays(1 & 2) in a nested way
        # So as to have all possible combinations
        for var1 in nums1:
            for var2 in nums2:

                # Store the sum of elements of both the arrays in the Hash Table
                # Along with their frequencies
                if var1 + var2 in hashtable:
                    hashtable[var1 + var2] += 1
                else:
                    hashtable[var1 + var2] = 1

        # Declare an ans variable to increment the ans
        ans = 0

        # Traverse the next two (3 and 4) arrays in a nested way
        # So as to have all possible combinations
        for var3 in nums3:
            for var4 in nums4:

                # If Additive Inverser exist in the Hash Table
                # Add its frequency to the ans
                if -var3 - var4 in hashtable:
                    ans += hashtable[-var3 - var4]
        return ans


import bisect


class BinarySolution:
    def Four_Sum(self, nums1, nums2, nums3, nums4):
        """
        Interface
        ----
        :type nums1: list of int
        :type nums2: list of int
        :type nums3: list of int
        :type nums4: list of int
        :rtype: int

        Approach
        ----
        Binary Search Approach
        1. In this approach , We first take the sum of each elements of array 1 and 2 in a single array
        and similarly array 3 and 4 in another array. 

        2. The newly created array will be of size n^2. 

        3. Then we sort one of the newly created array. 

        4. From each element of another array we search for its additive inverse using Binary Search.

        Complexity
        ----
        Time : O(n^2 + n^2*log(n^2) + n^2*log(n^2)) -> O(n^2*log(n^2))
        Space : O(n^2)
        """
        # Define an ans var and initialise it to 0 for storing the ans
        ans = 0

        # sum1_2 stores the sum of each combination of elements of array 1 and 2
        sum1_2 = []
        # sum3_4 stores the sum of each combination of elements of array 3 and 4
        sum3_4 = []

        # Find the length of each array (each array's length is same)
        n = len(nums1)

        # Traverse the array in nested way
        # So as to store each combination
        for i in range(n):
            for j in range(n):
                sum1_2.append(nums1[i] + nums2[j])
                sum3_4.append(nums3[i] + nums4[j])

        # Sort the sum3_4 array
        # To perform binary search
        sum3_4.sort()

        # Traverse the sum1_2 array
        for pair in sum1_2:

            # bisect_left is used to get the first index of the variable passed
            # NOTE: we need to look for -pair because we want to sum to zero
            left_idx = bisect.bisect_left(sum3_4, -pair)

            # bisect_right is used to get the last index of the variable passed
            right_idx = bisect.bisect_right(sum3_4, -pair)

            # If the element exists
            # Increment the ans
            if left_idx != -1:
                ans += (right_idx - left_idx)

        return ans


n1 = [3, 2, 1]
n2 = [4, -1, -2]
n3 = [-1, 2, -4]
n4 = [2, 0, 3]

s = BinarySolution()
print(s.Four_Sum(n1, n2, n3, n4))

"""
BISECT UNDERSTANDING
"""

# Python code to demonstrate the working of
# bisect(), bisect_left() and bisect_right()

# importing "bisect" for bisection operations
import bisect

# initializing list
li = [1, 3, 4, 4, 4, 6, 7]

# using bisect() to find index to insert new element
# returns 5 ( right most possible index )
print("The rightmost index to insert, so list remains sorted is  : ", end="")
print(bisect.bisect(li, 4))

# using bisect_left() to find index to insert new element
# returns 2 ( left most possible index )
print("The leftmost index to insert, so list remains sorted is  : ", end="")
print(bisect.bisect_left(li, 4))

# using bisect_right() to find index to insert new element
# returns 4 ( right most possible index )
print("The rightmost index to insert, so list remains sorted is  : ", end="")
print(bisect.bisect_right(li, 9, 0, 3))
