"""
Decode Ways
Given a string s that represents a special encoding, return the total ways that s can be decoded
using an alphabetic encoding from 1-26 corresponding to the letters from a-z.

The mapping is like so:
1 -> "a"
2 -> "b"
3 -> "c"
...
12 -> "l"
13 -> "m"
14 -> "n"
...
22 -> "v"
23 -> "w"
24 -> "x"
25 -> "y"
26 -> "z"

Example 1:
Input: "123"
Output: 3
Explanation:
There are 3 possible valid & complete decodings:
1.) ["1", "2", "3"] =>["a", "b", "c"]
2.) ["12", "3"] => ["l", "c"]
3.) ["1", "23"] => ["a", "w"]

Example 2:
Input: "33"
Output: 1
Explanation:
There is 1 possible valid & complete decoding:
1.) ["3", "3"] =>["c", "c"]

Constraints:
0 <= len(s)<= 100
The string will only digits 1 to 9
"""


class Solution:
    def decodeWays(self, s):
        """
        Interface
        ----
        :type s: str
        :rtype: int

        Approach
        ----
        1. Construct the solution using a recursive tree
        - identify subproblems (ie. sequences of numbers and associated mappings)

        2. Make use of a cache to trim the tree

        3. Identify the base cases

        Complexity
        ----
        Recurrence relation 
        N = len(s)
        T(N) = T(N-1) + T(N-2) + O(1)
        NOTE: the helper function has constant time

        Time : O(2^N) ie. the deepest part of the tree will be N function calls deep.
        With memoization the time complexity becomes O(N) because we cache answers and only solve subproblems once
        Space : O(N) because we keep a table with N subproblems
        """
        dp = [-1] * len(s)

        return self.num_decodings(s, 0, dp)

    def num_decodings(self, s, decode_pointer, dp):
        # NOTE: BASE CASE
        if decode_pointer >= len(s):
            return 1  # "" is a valid decomposition. ie. we have reached a full decomposition

        # Subproblem already solved and has a value
        if dp[decode_pointer] > -1:
            return dp[decode_pointer]

        # exists in this stack frame
        total_decompositions = 0

        # For substrings of length 1 and 2
        # NOTE: we can only have encodings with two numbers as we have a-z <-> 1-26
        for i in range(1, 3):
            # we have to make sure we don't go past the end of the string
            # NOTE: this ensures our snippet only includes what's in the string
            if decode_pointer + i <= len(s):
                # Grab the substring of length 1 and 2 if they exist starting from decodePointer
                snippet = s[decode_pointer:decode_pointer + i]

                # If the snippet is valid
                # Make recursive call
                # And assign its value to totalDecompositions
                if self.is_valid(snippet):
                    total_decompositions += self.num_decodings(
                        s, decode_pointer + i, dp)

        # Record subproblem answer to decompositions from (decodePointer)...(s.length - 1)
        dp[decode_pointer] = total_decompositions

        return dp[decode_pointer]

    # Helper function to check weather the snippet is valid
    def is_valid(self, s):

        # Case when string is empty or 0 occur at begining
        if len(s) == 0 or s[0] == "0":
            return False

        value = int(s)

        # Value of valid snippets lie between 0 and 26
        # 1 -> a
        # 26 -> z
        return value >= 1 and value <= 26


Str = "123"
soln = Solution()
print(soln.decodeWays(Str))
