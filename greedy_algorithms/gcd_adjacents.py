"""
GCD Adjacents
A divisor is a number that divides into another without a remainder.

A greatest common divisor is the greatest number that is a shared divisor between two numbers.

Given an array A[] of integers, you are allowed to perform the following operation several times:
Choose two indices i and j and replace exactly one of A[i] or A[j] with the greatest common divisor of A[i] and A[j].

What is the minimum number of operations you need to perform so that all of the elements in A[] equal 1?

Return -1 if it is impossible to use the described operation to end up with an array with only ones.

Example #1:
Input: [2, 1, 1, 1]
Output: 1
Explanation: We can choose indices i = 0 and j = 1 and replace A[0] (whose previous value was 2) with gcd(A[0], A[1]), which equals 1. The resulting array becomes [1, 1, 1, 1]. At this point, we are done.

Example #2:
Input: [2, 4, 6, 8]
Output: -1
Explanation: No matter how many times we perform the described operation, we will never result in an array with all ones. The GCD of the whole array is 2.
"""


class Solution:
    def gcdAdjacents(self, A):
        """
        Interface
        ----
        :type A: list of int
        :rtype: int

        Approach
        ----
        1. First of all, note that if the greatest common divisor of every element in the array does not equal one, 
        then an answer does cannot exist (the greatest common divisor of two adjacent elements will not equal one). 

        2. Next, a key observation is that an absolute lower bound on the minimum number of operations we must perform is equal
        to the number of non-one elements in our array. 

        NOTE: This is true because an optimal solution must perform at least one operation in order to make the non-one element equal to one. 
        For example, we immediately know that the minimum number of operations to make the elements of the array [1, 3, 5] will be at least two
        since there are exactly two elements that are not equal to one. 

        3. Now if our array starts off with at least one element equal to one, then we can attain the previously described lower bound by using
        this element to make the other elements equal to one. As an example, if our initial array is [5, 5, 1, 5, 5], then we require exactly four operations.

        4. In each operation, we convert one of the fives adjacent to a one equal into a one. 

        5. Conversely, if our array does not have a one, then we want to find the smallest subarray such that the greatest common divisor among all of the
        elements equals one. NOTE: This subarray's length will tell us the minimum number of operations we need to perform in order to obtain a one in our array. 

        6. From here, we can simply use this one to convert all of our other elements into ones. The total number of operations we perform in this case is the number
        of operations needed to obtain the one plus the number of operations needed to convert the remaining elements into one.

        Complexity
        ----
        Time : O(N^2)
        Space : O(1)
        """
        N = len(A)

        # If our array contains a single "1" in the array, then we can make
        # other elements equal to "1" using this element.
        num_ones = 0
        for i in range(0, N):
            if A[i] == 1:
                num_ones += 1

        # Case when frequency of '1' is greater than 0
        # NOTE: the difference N - num_ones is the lower bound
        if num_ones > 0:
            return N - num_ones

        # There are no ones in the array; let's find the smallest
        # contiguous subarray whose GCD equals 1.
        smallest_region = N + 1

        # Nested loop for checking the gcd of each region
        for left in range(0, N):
            # root our scanning window
            current_gcd = A[left]
            # right is the linear scanning pointer to check for GCDs
            for right in range(left, N):
                current_gcd = self.computeGCD(current_gcd, A[right])

                # If we get gcd of any region as 1
                # Update the smallest_region if current region is smaller
                if current_gcd == 1:
                    smallest_region = min(smallest_region, right - left + 1)
                    # this break statement will take us back to the top of the
                    # outer for loop, there is no need to keep checking
                    break

        # No region exists
        if smallest_region == N + 1:
            return -1

        # total_operations = operations_obtain_one + len(arr) - 1
        # ie. once we have a single one we have len(arr) - 1 non-one entries
        return (smallest_region - 1) + (N - 1)

    # Helper function to compute the GCD of 2 numbers
    def computeGCD(self, x, y):

        # Method used is called the Euclidean Algorithm
        while x != 0 and y != 0:
            if x > y:
                x %= y
            else:
                y %= x

        return y if x == 0 else x


arr = [3, 4, 6, 8]
# we expect the smallest sub array with a GCD of 1 to be 2
# so the final answer is 5

s = Solution()
# finding the GCD with a Euclidean algorithm
print(s.computeGCD(5, 2))
out = s.gcdAdjacents(arr)
print(out)
