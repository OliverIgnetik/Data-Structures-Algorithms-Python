"""
Levenshtein Distance
Given two strings s1 and s2, we would like to find the minimum "transformation" distance it would take to transform s1 into s2.

There are many variants of edit distance metrics for comparing strings. We will specifically be looking at what
is formally called the levenshtein distance between two strings.

CONSTRAINTS
NOTE: You have 3 transformations available to you to turn s1 into s2:
Inserting a character
Deleting a character
Replacing a character

Each has a cost of 1 to perform.

Here are some transformation examples to get you more acquainted:

Example 1:
Input: s1 = "a", s2 = "bba"
Output: 2
Explanation: 
"a" -> "ba" (insert 'b' to the start)
"ba" -> "bba" (insert 'b' to the start)

Example 2:
Input: s1 = "a", s2 = "b"
Output: 1
Explanation: 
"a" -> "b" (replace 'a' with 'b')

Example 3:
Input: s1 = "intention", s2 = "execution"
Output: 5
Explanation:
"intention" -> "inention" (delete 't')
"inention" -> "enention" (replace 'i' with 'e')
"enention" -> "exention" (replace 'n' with 'x')
"exention" -> "exection" (replace 'n' with 'c')
"exection" -> "execution" (insert 'u')

Given these 2 strings s1 and s2, compute their Levenshtein Distance.

Follow-Up
After your algorithm computes the Levenshtein Distance (which is just a number), can it find the actual path of transformations from start to end?

Hint: The dp table/cache is all you need

Constraints:
0 <= s1.length <= 100
0 <= s2.length <= 100
"""


class Solution:
    def levenshteinDistance(self, s1, s2):
        """
        Interface
        ----
        :type s1: str
        :type s2: str
        :rtype: int

        Approach 
        ----
        1. Draw the recursive tree

        2. Build the subproblem table

        3. Identify the subproblem problem relations
        - ie. how does each operation relate to the subproblem table?

        4. Identify base cases

        Complexity
        ----
        Top Down 
        Time : O(s1*s2) with memoization we trim the recursion tree quite significantly from O(3^N)
        NOTE: O(3^N) assumes that N chars are all different and thus is the maximum height of the recursion tree
        Space : O(s1*s2) we have a cache just as we do in the bottom-up solution

        Bottom Up
        Time : O(s1*s2)
        Space : O(s1*s2) we have a cache
        """

        # Initialise the 2D array with -1
        opt = [[-1 for x in range(len(s2))] for x in range(len(s1))]

        return self.levenshtein_distance_top_down(s1, len(s1) - 1, s2, len(s2) - 1, opt)

    def levenshtein_distance_top_down(self, s1, s1_index, s2, s2_index, opt):
        if s1_index < 0:
            return s2_index + 1  # If s1 is "", it is all insertions to get s1 to s2
        elif s2_index < 0:
            return s1_index + 1  # If s2 is "", it is all deletions to get s1 to s2

        # If we have already calculated the value
        # This stops recomputing the same value
        if opt[s1_index][s2_index] != -1:
            return opt[s1_index][s2_index]

        if (s1[s1_index] == s2[s2_index]):
            # Characters match - no repair needs to take place, no addition to distance
            # NOTE: the answer to this subproblem is the same as the case with both
            # letters removed ie. s1_index - 1 and s2_index - 1
            opt[s1_index][s2_index] = self.levenshtein_distance_top_down(
                s1, s1_index - 1, s2, s2_index - 1, opt)
        else:

            """
            We have a character mismatch. Remember we want to transform s1 into s2 and
            we hold the i'th character of s1 and the j'th character of s2:

            Deletion:
                Find levenshtein distance of s1[0...(i-1)] => s2[0...j]
                i'th character of s1 is deleted
            Insertion:
                Find levenshtein distance of s1[0...i] => s2[0...(j-1)]
                We then insert s2[j] into s2 to regain s2[0...j]
            Substitution:
                Find levenshtein distance of s1[0...(i-1)] => s2[0...(j-1)]
                We then insert s2[j] as i'th character of s1 effectively substituting it
            """
            # delete
            delete = self.levenshtein_distance_top_down(
                s1, s1_index - 1, s2, s2_index, opt)
            # insert
            insert = self.levenshtein_distance_top_down(
                s1, s1_index, s2, s2_index - 1, opt)
            # substitute
            substitute = self.levenshtein_distance_top_down(
                s1, s1_index - 1, s2, s2_index - 1, opt)

            # We want to take the minimum of these 3 options to fix the problem (we add
            # to the min cost action to symbolize performing the operation)
            opt[s1_index][s2_index] = 1 + min(delete, min(insert, substitute))

        return opt[s1_index][s2_index]


s1 = "intention"
s2 = "execution"
print(Solution().levenshteinDistance(s1, s2))
