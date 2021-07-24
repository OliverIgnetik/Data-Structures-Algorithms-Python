"""
DNA Sequence Alignment
Sequence alignment use in the discipline of bioinformatics to align DNA sequences for analysis and the discovery of diverging patterns.

An "alignment" is a matching of each character between s1 and s2 to a character in the other string, or a gap.

NOTE: ALLOWABLE OPERATIONS
To fix character mismatches when aligning s1 and s2 we may perform 3 operations.
Match the character in s1 to a gap (this puts a gap in s2)
Match the character in s2 to a gap (this puts a gap in s1)
Take a predefined mismatch cost and match the mismatching characters together anyway

NOTE: Our costs are:
GAP_COST: Gaps cost 1 abstract unit of cost
MISMATCH(c1, c2): Mismatches' cost is predefined and can be found with an O(1) lookup to the table mismatchCosts provided as a parameter
NOTE: If c1 = c2 then MISMATCH(c1, c2) = 0 (same character, no cost to match them together)

Given two strings s1 and s2, calculate the minimum cost to "align" the two strings.

Example 1:
Input:
s1 = "GACGTTA"
s2 = "GAACGCTA"

Output: 3
Explanation:

The possible minimum alignment looks like so:

"GA_CG_TTA"
"GAACGCT_A"

We take 3 gaps and all other matchings between characters match to the equivalent characters. So our overall gap cost is 3 and our overall mismatch cost is 0. So the overall alignment cost is 3.
"""


class Solution:
    GAP_COST = 1
    alignment_costs = {}

    def __init__(self):
        self.initialize_alignment_costs()

    def minCostAlignment(self, s1, s2):
        """
        Interface
        ----
        :type s1: str
        :type s2: str
        :rtype: int

        Approach
        ----
        1. Identify subproblems

        2. Establish subproblem relations and how they correspond to operations

        NOTE: SUB PROBLEM COMPETITION
        opt(i, j) = min(
            alignment    alignment_cost(s1[i],s2[j]) + opt(i-1, j-1),      
            gap in s1    GAP_COST + opt(i, j-1),
            gap in s2    GAP_COST + opt(i-1, j),
        )

        NOTE: when we choose to place a gap in s1 we are saying the char residing at j in s2 was matched to a gap.
        Then we just need to match the rest of s2 (j-1) to everything still in s1 (i)

        s1 = 0, ..., i
        s2 = 0, ..., j

        3. Identify base cases

        4. Cache structure

        rows = index in s1
        columns = index in s2

        Complexity
        ----
        Time : O(s1*s2) pseudopolynomial 
        Space : O(s1*s2)
        """
        # establish subproblem table
        opt = [[0 for x in range(len(s2) + 1)] for x in range(len(s1) + 1)]

        # base cases
        # NOTE: we can only choose to insert a gaps if we are aligning a string with an empty string
        for row in range(0, len(s1) + 1):
            opt[row][0] = row * Solution.GAP_COST

        # base cases
        # NOTE: we can only choose to insert a gaps if we are aligning a string with an empty string
        for col in range(0, len(s2) + 1):
            opt[0][col] = col * Solution.GAP_COST

        for row in range(1, len(s1) + 1):
            for col in range(1, len(s2) + 1):
                # get the comparison signature
                combined = s1[row - 1] + s2[col - 1]
                # retrieve the alignment cost
                alignment_cost = self.alignment_costs[combined]

                # NOTE: subproblem competition
                # adds pair to conceptual matching set
                align = alignment_cost + opt[row - 1][col - 1]
                # leaves a gap in s2, match s1 char to gap so lose a character from s1
                dont_match_s1_char = Solution.GAP_COST + opt[row - 1][col]
                # leaves a gap in s1, match s2 char to gap so lose a character from s2
                dont_match_s2_char = Solution.GAP_COST + opt[row][col - 1]

                # take the minimum
                opt[row][col] = min(align, min(
                    dont_match_s1_char, dont_match_s2_char))

        return opt[len(s1)][len(s2)]

    def initialize_alignment_costs(self):
        self.alignment_costs["AA"] = 0
        self.alignment_costs["CC"] = 0
        self.alignment_costs["GG"] = 0
        self.alignment_costs["TT"] = 0

        '''
        Costs arbitrarily chosen. Symmetry shouldn't guarantee same
        alignment cost because character 1 is from s1 and character
        2 is from s2. So "AC" could theoretically cost more(or less)
        to align than "CA".
        '''
        self.alignment_costs["AC"] = 1
        self.alignment_costs["CA"] = 1

        self.alignment_costs["AG"] = 2
        self.alignment_costs["GA"] = 2

        self.alignment_costs["AT"] = 4
        self.alignment_costs["TA"] = 4

        self.alignment_costs["CG"] = 3
        self.alignment_costs["GC"] = 3

        self.alignment_costs["CT"] = 5
        self.alignment_costs["TC"] = 5

        self.alignment_costs["GT"] = 1
        self.alignment_costs["TG"] = 1


s1 = "GACGTTA"
s2 = "GAACGCTA"

print(Solution().minCostAlignment(s1, s2))
