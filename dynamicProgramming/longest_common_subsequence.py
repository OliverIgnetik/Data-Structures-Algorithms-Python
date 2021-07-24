"""
Longest Common Subsequence
Given two strings s1 and s2 return the length of the longest common subsequence of characters between the two strings.

Example 1:
Input:
s1 = "ABCD"
s2 = "ABCD"

Output: 4
Explanation:
"ABCD"
"ABCD"
Both strings share the subsequence "A", "B", "C", "D".

Example 2:
Input:
s1 = "ADC"
s2 = "ABCD"

Output: 2
Explanation:
"ADC"
"ABCD"
Both strings share the subsequence "A", "D".

Example 3: subsequences don't have to be contiguous
Input:
s1 = "ABCDGH"
s2 = "AEDFHR"

Output: 3 
Explanation:
ABCDGH
_  _ _

AEDFHR
_ _ _

"""


class BottomUpSolution:
    def longestCommonSubsequenceLength(self, s1, s2):
        """
        Interface
        ----
        :type s1: str
        :type s2: str
        :rtype: int

        Approach
        ----
        1. Break down call recursion tree 

        2. Identify the recurrence relation and the relations of subproblems

        3. Identify base cases

        Complexity
        ----
        Time : O(s1*s2) trims the recursion call tree down from O(3^N) where N is max(s1,s2)
        Space : O(s1*s2)
        """

        """
        * s2 will be on the rows, s1 will be on the columns.
        * 
        * +1 to leave room at the left for the "".
        """
        cache = [[0 for i in range(0, len(s1) + 1)]
                 for i in range(0, len(s2) + 1)]

        """
        * cache[s2.length()][s1.length()] is our original subproblem. Each entry in the
        * table is taking a substring operation against whatever string is on the rows
        * or columns.
        * 
        * It goes from index 0 to index s2Row/s1Col (exclusive)
        * 
        * So if my s1 = "azb" and s1Col = 2...then my substring that I pass to the
        * lcs() function will be:
        * 
        * 0 1 2 "a  z  b"
        * 
        * "az" (index 2...our upper bound of the snippet...is excluded)
        
        """

        for s2Row in range(0, len(s2) + 1):
            for s1Col in range(0, len(s1) + 1):
                # base case
                if (s2Row == 0 or s1Col == 0):
                    cache[s2Row][s1Col] = 0
                # matching characters
                elif (s2[s2Row - 1] == s1[s1Col - 1]):
                    cache[s2Row][s1Col] = cache[s2Row - 1][s1Col - 1] + 1
                else:
                    # NOTE: subproblem competition
                    # we take the max from either stripping one char from s1 or s2
                    cache[s2Row][s1Col] = max(
                        cache[s2Row - 1][s1Col], cache[s2Row][s1Col - 1])

        return cache[len(s2)][len(s1)]


class TopDownSolution:

    def longestCommonSubsequenceLength(self, s1, s2):
        """
        Interface
        ----
        :type s1: str
        :type s2: str
        :rtype: int

        Approach
        ----
        1. Break down call recursion tree 

        2. Identify the recurrence relation and the relations of subproblems

        3. Identify base cases

        Complexity
        ----
        Time : O(s1*s2) memoization trims the recursion call tree down from O(3^N) where N is max(s1,s2)
        Space : O(s1*s2)
        """

        # Helper function for recursion
        def lcs(n, m, cache):
            '''
            * Base Case
            * 
            * lcs("", anything...) == 0 lcs(anything..., "") == 0 lcs("", "") == 0
            * 
            * A subproblem where either string is empty will have a result of 0. There can
            * be nothing in common with an empty string and anything else.
            '''
            if n == 0 or m == 0:
                return 0

            # If we have already computed this
            # It stops further recursion and stops computing same value again and again
            if cache[n - 1][m - 1] != -1:
                return cache[n - 1][m - 1]

            s1FinalCharacter = s1[n - 1]
            s2FinalCharacter = s2[m - 1]

            # No competition necessary. A match. The answer to THIS subproblem is 1 PLUS
            # the best answer to the subproblem without either of these characters.
            if s1FinalCharacter == s2FinalCharacter:
                cache[n - 1][m - 1] = 1 + lcs(n - 1, m - 1, cache)

            # Character mismatch. Compete subproblems, whoever wins becomes the answer to
            # this subproblem and is hence returned
            else:
                cache[n - 1][m -
                             1] = max(lcs(n - 1, m, cache), lcs(n, m - 1, cache))

            return cache[n - 1][m - 1]

        # Initialise a 2D array with NULL
        cache = [[-1 for j in range(len(s2))] for i in range(len(s1))]
        return lcs(len(s1), len(s2), cache)


s1 = "ABCD"
s2 = "ABCD"
sT = TopDownSolution()
sB = BottomUpSolution()
print(sT.longestCommonSubsequenceLength(s1, s2))
print(sB.longestCommonSubsequenceLength(s1, s2))
