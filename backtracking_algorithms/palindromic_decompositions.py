"""
Palindromic Decompositions
Given a string s, return all of its palindromic decompositions.

A "palindromic decomposition" is a splitting of the string into segments such that each segment is a palindrome.

Example 1:
Input: "a"
Output:
[
  ["a"]
]
Explanation: A single character is a palindrome, there is only one decomposition here.

Example 2:
Input: "aab"
Output:
[
  ["a", "a", "b"],
  ["aa", "b"]
]
Explanation: There are 2 decompositions. Each element of a decomposition is a palindrome. Each decomposition segments the original string.

Constraints:
0 <= len(s) <= 30
"""

from copy import deepcopy


class Solution:
    def partition(self, s):
        """
        Interface
        ----
        :type s: str
        :rtype: list of list of str

        Complexity
        ----

        Time :  O(2^N)
        NOTE: Powerset bound O(2^(N-1)) is the very loose bound. ie. we have N-1 decisions
        At each stack frame we can make N-1 snippets

        Space : O(N) call stack can have depth N
        """
        decompositions = []

        self.decompose_string(0, s, [], decompositions)

        return decompositions

    # Helper function for recursively calculating the ans
    def decompose_string(self, working_index, s, partial_decomposition, decompositions):

        # If we have decomposed the whole string then reap the
        # 'partialDecomposition', it is now complete.
        if working_index == len(s):
            # we need to make a deepcopy of the partial decomposition
            # at this stack frame
            decompositions.append(deepcopy(partial_decomposition))
            return

        # Take every snippet take from the 'workingIndex' to the end of the
        # string. This is our 'possibility space' that we can recurse into.
        # go all the way until the end of the string
        for i in range(working_index, len(s)):

            # Constraint - Only recurse if the snippet from 'workingIndex' (inclusive) to
            # s.length() (inclusive) is a palindrome
            # NOTE: if we guarantee this the base case will be palindromic
            if self.is_palindrome(working_index, i, s):

                # Choose - Take the snippet & add it to our decomposition 'path'
                partial_decomposition.append(s[working_index:i + 1])

                # Explore - Recurse and advance progress 1 past right bound of
                # the 'palindromicSnippet' which is 'i + 1'
                self.decompose_string(
                    i + 1, s, partial_decomposition, decompositions)

                # Unchoose/BACKTRACK - We are done searching, remove the snippet from our 'path'.
                # NOTE: Next loop iteration will try another snippet in this stackframe.
                partial_decomposition.pop()

    # Checks if the region from left (inclusive) to right (inclusive) is
    # a palindromic.
    def is_palindrome(self, left, right, s):
        """
        Complexity
        ----
        Time : O(N)
        Space : O(1)
        """
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True


i = "aab"
s = Solution()
print(s.partition())
