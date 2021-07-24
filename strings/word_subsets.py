"""
Example 1:
Input:
A = ["orange", "room", "more"]
B = ["rm", "oo"]

Output: ["room"]

Explanation:
- "orange" is missing an "m" so it is not a superset of "rm". It also only has one "o" so it is not a superset of "oo".
- "room" is a superset of "rm" and "oo". All strings in B are in "room", so "room" is universal.
- "more" is a superset of "rm" since it has an "m" and an "r". It only has one "o" so it is not a superset of "oo".

Example 2:
Input:
A = ["padding", "css", "randomcs"]
B = ["cs", "c"]

Output: ["css", "randomcs"]
"""

from typing import List
from collections import Counter


class Solution:
    def check_superset(self, candidate: str, B_hashmaps: List[dict]) -> bool:
        c1 = Counter(candidate)
        # building this c2 counter is replicated work
        for hashmap in B_hashmaps:
            for key in hashmap:
                if key not in c1 or (not (c1[key] >= hashmap[key])):
                    return False

        return True

    def word_subsets(self, A: List[str], B: List[str]) -> List[str]:
        """
        Complexity
        ----
        a = length of array A
        b = length of array B
        m = longest string in A
        k = longest string in B

        Time : O(b*k + a*m)
        Space : O(b*k)
        """
        res = []
        B_hashmaps = []
        for word in B:
            B_hashmaps.append(Counter(word))

        for word in A:
            if self.check_superset(word, B_hashmaps):
                res.append(word)
        return res


class AlternativeSolution:
    def wordSubsets(self, A, B):
        '''
        :type A: list of str
        :type B: list of str
        :rtype: list of str
        '''
        b_count = [0] * 26

        # Collecting the constraints into a character mapping
        # Store the maximum number of each character
        # That will be required for string to be power set
        for word in B:
            tmp_count = self.count(word)

            for i in range(0, 26):
                b_count[i] = max(b_count[i], tmp_count[i])

        # Testing each character in A
        # For each string in A
        # Check if it contains frequency greater than or equal to required
        output = []
        for word in A:
            tmp_count = self.count(word)

            universal = True
            for i in range(0, 26):
                if tmp_count[i] < b_count[i]:
                    universal = False

            if universal:
                output.append(word)

        return output
    # Helper function to count the frequency of letters

    def count(self, word):
        output = [0] * 26

        for letter in word:
            idx = ord(letter) - ord("a")
            if idx >= 0:
                output[idx] += 1

        return output


A = ["padding", "css", "randomcs"]
B = ["cs", "c"]
s = Solution()

print(s.word_subsets(A, B))
