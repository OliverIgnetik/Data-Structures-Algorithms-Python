
from typing import List


class Solution:
    def make_signature(self, word: str) -> int:
        """
        If the signature does not depend on order 
        a sum is a good way to do it. 
        NOTE: we need to include things that anagrams have in common 
        - the frequency in which letters appear
        - length of the string
        - we could sort the dictionary but that would significantly increase 
        the time complexity with O(NlogN) operations
        """
        signature = [0] * 26
        m = {}
        for char in word:
            val = ord(char) - ord('a')
            signature[val] += 1

        return str(signature)

    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        '''
        :type words: list of str
        :rtype: list of list of str

        Complexity
        ----
        N = length of words array
        k = longest word with all unique letters
        Time : O(N*k)
        Space : O(N)
        '''

        m = {}
        for i, word in enumerate(words):
            signature = self.make_signature(word)
            if signature not in m:
                m[signature] = [i]
            else:
                m[signature].append(i)

        # return each of the groupings
        res = []
        for key in m:
            anagram_group = []
            for i in m[key]:
                anagram_group.append(words[i])
            res.append(anagram_group)
        return res


s = Solution()
words = ["eat", "bat", "ate", "tab", "tea", "eat"]
print(s.groupAnagrams(words))
