"""
Verifying Character Ordering
Given a string s representing a new ordering of the lowercase English letters and an array A[] of strings,
return true if and only if A[] is sorted in lexicographical order according to the ordering provided in s.

Example #1:
Input: s = "hlbcdefgijkmnopqrstuvwxzya", A[] = ["hello", "hey", "a"].
Output: true
Explanation: Under the new ordering, the array A[] is sorted. Note that the letter 'h' comes before the letter 'a', and the letter 'l' comes before the letter 'y'. 
"""


class Solution:
    """
    Approach
    ----
    Using Characters as Indices
    1. We can keep an array of size 26 and effectively map each of the 26 lowercase characters to the index at which they appear in our ordering. 

    2. The motivation behind creating such a map is that it allows us to compare two characters and determine their relative ordering in O(1) time. 

    3. More precisely, to determine whether some character c1 is smaller than some character c2, we can simply use c1 and c2 as
    indices in our array and compare the integer values stored at these entries. 

    4. In order to help us determine if our array of string is sorted, we create a helper function that takes in two strings
     and returns true if and only if the first string compares less than the second string (according to the ordering provided).

    5. As a reminder, recall that a string s1 is lexicographically smaller than another string s2 if and only if s1 is a prefix
    of s2 or the character in s1 at the first index at which s1 and s2 differ compares less than the character at the same index in s2.

    6. In the implementation provided, we compare two strings done by comparing the strings character-by-character until either the
    strings differ or at least one string runs out of characters. 

    7. In either case, we can immediately conclude the strings' relative lexicographical ordering. 

    8. From here, we use this helper method to compare successive strings in the inputted array to verify that the array is in sorted order. 
    If we find a pair of adjacent indices at which the array is not sorted, we can immediately return false. 

    9. Otherwise, if we finish processing the entire array without returning, we return true.

    Complexity
    ----
    Time : O(N) 
    Space : O(1) 
    """

    # Helper function which
    # Compares two strings with the new ordering. Returns true if s1 is before s2
    def compareStrings(self, table, s1, s2):
        counter = 0

        # Traverse till the minimum size of both the strings
        # Return true and false accordingly
        while(counter < len(s1) and counter < len(s2)):
            if(s1[counter] != s2[counter]):
                return table[s1[counter]] < table[s2[counter]]
            counter = counter + 1

        # If all characters till min(n,m) were same of both the strings
        return len(s1) <= len(s2)

    def verifyOrdering(self, A, ordering):
        # Maps each character to its respective order
        table = {}
        for i in range(0, len(ordering)):
            table[ordering[i]] = i

        # Iterates through list of strings to verify that they are in order
        # we need to iterate to the second to last item
        for i in range(0, len(A) - 1):
            # If the next string comes before the current string, then return false
            if self.compareStrings(table, A[i], A[i + 1]) == False:
                return False

        return True


# s encodes the lexographical ordering
s = "hlbcdefgijkmnopqrstuvwxzya"
A = ["hello", "hey", "a"]

print(Solution().verifyOrdering(A, s))
