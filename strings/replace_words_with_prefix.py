
"""
Inputs:
prefixes = ["cat", "catch", "Alabama"]
sentence = "The cats were catching yarn"

Output: "The cat were cat yarn"
Explanation: "cats" and "catching" were both replaced by their shortest prefix match "cat"
Shortest prefix wins when there are multiple matches
"""
from typing import List


class Solution:
    def prefix_match(self, word: str, prefixes: List[str]) -> str:
        shortest_prefix = float('inf')
        index = 0
        found = False
        for i, prefix in enumerate(prefixes):
            if len(prefix) < shortest_prefix and word.startswith(prefix):
                shortest_prefix = len(prefix)
                index = i
                found = True
        if found:
            return prefixes[index]
        else:
            return None

    def replaceWordsWithPrefix(self, sentence: str, prefixes: List[str]) -> str:
        """
        Complexity
        ----
        N = number of words in the sentence
        K = longest prefix length 
        M = Number of Prefixes

        Time : O(N*K*M) Upper bound is that every word in the sentence could have 
        length greater then or equal to the longest prefix
        Space : O(N*K) Including the output

        NOTE: This solution is less efficient because we have to do a linear scan of the 
        prefix array. Using a hashtable is better because of the constant look up
        """
        sentence_list = sentence.split(' ')

        for i, word in enumerate(sentence_list):
            prefix_match = self.prefix_match(word, prefixes)
            if prefix_match:
                sentence_list[i] = prefix_match
        return ' '.join(sentence_list)


class AlternativeSolution:
    def replaceWordsWithPrefix(self, sentence: str, prefixes: List[str]) -> str:
        """
        Complexity
        ----
        N = len(S)
        M = number of prefixes
        k = Maximum length prefix
        Time : O(max(N^2, M)) 
        Space : O(max(N, M)) Including the output
        """
        words = sentence.split(' ')
        m = dict()

        for prefix in prefixes:  # O(M)
            m[prefix] = True

        for i, word in enumerate(words):  # O(N)
            # find the shortest prefix
            for j, let in enumerate(word):  # O(N) we could have one really long word

                if word[0:j] in m:  # O(k) sub string scanning
                    words[i] = word[0:j]
                    break
        return ' '.join(words)


prefixes = ["cat", "catch", "Alabama"]
sentence = "The cats were catching yarn"

s1 = Solution()
s2 = AlternativeSolution()
print(s1.replaceWordsWithPrefix(sentence, prefixes))
print(s2.replaceWordsWithPrefix(sentence, prefixes))
