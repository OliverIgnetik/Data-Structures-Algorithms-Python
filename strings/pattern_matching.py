from typing import List


class Solution:
    def match(self, s: str, pattern: str) -> bool:
        pattern_dic = {}
        for i, l in enumerate(pattern):
            if l not in pattern_dic:
                pattern_dic[l] = [i]
            else:
                pattern_dic[l].append(i)

        s_dic = {}
        for i, l in enumerate(s):
            if l not in s_dic:
                s_dic[l] = [i]
            else:
                s_dic[l].append(i)

        # edge case
        if len(s_dic) != len(pattern_dic):
            return False

        s_l = list(s_dic.values())
        p_l = list(pattern_dic.values())

        # general case
        for i in range(len(s_l)):
            if s_l[i] != p_l[i]:
                return False

        return True

    def pattern_matching(self, lst: List[str], pattern: str) -> List[str]:
        """
        Input 
        ----
        lst : list of strings 
        pattern : str for pattern matching

        Output 
        ----
        res : list of strings that match pattern

        Approach 
        ----
        How do we encapsulate the pattern?

        Complexity 
        ----
        k = the longest word length
        Time : O(Nk)
        Space : O(Nk) including output
        """
        res = []
        for s in lst:
            if self.match(s, pattern):
                res.append(s)
        return res


class AlternativeSolution:

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        '''
        :type words: list of str
        :type pattern: str
        :rtype: list of str
        '''
        matches = []
        # len is length of the
        # pattern
        Len = len(pattern)

        # Encode the string
        hash = self.encodeString(pattern)

        # Iterate through the array of strings
        for word in words:

            # If the returned hash is same and size is same than append to ans
            if(len(word) == Len and
                    self.encodeString(word) == hash):
                matches.append(word)
        return matches

    def encodeString(self, Str: str) -> str:

        map = {}
        res = ""
        i = 0

        # Iterate through each character in the given string
        for ch in Str:

            # If the char is occuring first time , assign next unique number to it
            if ch not in map:
                map[ch] = i
                i += 1

            res += str(map[ch])
        return res


s = Solution()
s_a = AlternativeSolution()

print(s.pattern_matching(["aac", "bbc", "bcb", "yzy"], "ghg"))
print(s_a.findAndReplacePattern(["aac", "bbc", "bcb", "yzy"], "ghg"))
