"""
String Transformations
Given a string beginWord, a string endWord, and a list of words words, return the total "transformations" it would take
to turn beginWord into endWord.

A "transformation" consists of a single character change in a string. Only words in words array can be used in the
transformation "path" starting at beginWord and terminating at endWord.

If a transformation path cannot be found, return -1.

Examples 1:
Input:
beginWord = "dog"
endWord = "lot"
words = ["dot", "mot", "lot"]

Output: 2
Explanation:
There are multiple paths following valid transformations:
1.) "dog" -> "dot" -> "mot" -> "lot"
2.) "dog" -> "dot" -> "lot"

The shortest path is the second with length 2.

Examples 2:
Input:
beginWord = "dog"
endWord = "lot"
words = ["dot"]

Output: -1
Explanation: There is no complete transformation path possible.
"dog" -> "dot -> ... no more words to get to "lot"

Constraints:
0 <= len(words) <= 100
"""

from typing import List
from collections import deque


class Solution:
    def build_word_relations(self, words: List[str], beginWord: str) -> dict:
        word_relations = {}
        words.append(beginWord)
        for word in words:
            for i in range(len(word)):
                signature = word[:i] + '*' + word[i + 1:]
                if signature in word_relations and word not in word_relations[signature]:
                    word_relations[signature].append(word)
                else:
                    word_relations[signature] = [word]

        return word_relations

    def get_neighbours(self, word: str) -> List[str]:
        neighbours = []
        for i in range(len(word)):
            signature = word[:i] + '*' + word[i + 1:]
            neighbour_candidates = self.word_relations[signature]
            for candidate in neighbour_candidates:
                if candidate not in neighbours and candidate != word:
                    neighbours.append(candidate)
        return neighbours

    def distance(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Input
        ----
        :type beginWord: str
        :type endWord: str
        :type wordList: list of str

        Output
        ----
        :rtype: int

        Approach 
        ----
        A single letter transformation means that the nodes for the associated words 
        are adjacent. 

        To find the shortest path possible we could use a BFS traversal.
        - ie. nodes that are two hops away from the source are 2 transformations away.

        NOTE: We could use Dijkstra's SSSP algorithm with all the edges weights set to 1 

        Complexity
        ----
        If W = length of word list
        L = Length of word
        Time : O(W*L)
        Space : O(W)
        """
        # edge case
        if endWord not in words:
            return -1
        # we need to store the relations in some manner
        self.word_relations = self.build_word_relations(words, beginWord)
        # we need to keep track of what words we have seen
        self.seen = set()
        q = deque()
        q.append([beginWord, 0])

        # commence BFS
        while len(q) != 0:
            word, transforms = q.popleft()
            # this is our goal
            if word == endWord:
                return transforms
            # if we have not seen this word then process
            if word not in self.seen:
                self.seen.add(word)
                neighbours = self.get_neighbours(word)
                for neighbour in neighbours:
                    if neighbour not in self.seen:
                        q.append([neighbour, transforms + 1])

        # there is no path that exists
        return -1


beginWord = "dog"
endWord = "lot"
words = ["dot", "mot", "lot"]
s = Solution()
print(s.distance(beginWord, endWord, words))
