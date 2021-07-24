"""
Decompose String
Given an array dictionary[] consisting of a list of non-empty words along with a string s, determine if s can be decomposed into a sequence of zero or more dictionary words.

Example 1:
Input: s = "apple", dictionary = ["ap", "pl", "ppp", "pple"]
Output: false
Explanation: No combination of words in our dictionary can be put together to form “apple”. The closest we can get is “appl”, which is missing the last "e" character ("e" is not in the dictionary).
"""


class Solution:
    def canDecompose(self, dictionary, s):
        """
        Interface
        ----
        :type dictionary: list of str
        :type s: str
        :rtype: bool

        Approach
        ----
        1. In order to solve this problem, we can use dynamic programming.

        2. The key observation is that, in order to decompose our string, 
        we must be able to decompose some (possibly empty) prefix of our string, 
        and the remaining suffix that must be a word in our dictionary. 

        NOTE: For example, if our dictionary is ["h", "e", "llo"] and we want to decompose the string
        "hello", then we are able to successfully decompose the prefix "he" (by using the words "h" and "e" 
        in our dictionary), and the remaining suffix ("llo") is a word in our dictionary. 

        3. Thus, we are motivated to keep a single dynamic programming state that indicates whether or not we
        are able to decompose a given prefix of our string.

        4. In other words, we can create an array of boolean variables called "possible[]" in which possible[i] 
        is set to true if and only if we can decompose the prefix s[1...i] of our original string.

        5. Our base case is possible[0] = true since we can always decompose the empty string by using no words
        from our dictionary at all. 

        6. To transition from one state to another, we can simply check whether we can append some word from our
        dictionary to the string obtained from a reachable state in order to achieve the new prefix being considered.

        Complexity
        ----
        The overall runtime is O(N*M), where N is the length of the original string and M is the size of our dictionary.
        If M is sufficiently larger than N, we can make a slight optimization by iterating over the possible strings in
        our dynamic programming table rather than our dictionary. 
        NOTE: The runtime of the modified approach would be O(N^2 + M).
        Time : O(N*M)
        Space : O(M)
        """

        # Set the 0 index to True since we can always decompose an empty string (this is our base case)
        can_decompose = [False] * (len(s) + 1)
        can_decompose[0] = True

        # We will utilize two pointers to check if substrings exist in our dictionary
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if can_decompose[j] == True and s[j:i] in dictionary:
                    # Update our array and break, since we have verified we can decompose our string up to index i
                    can_decompose[i] = True
                    break

        # Return true if we can decompose the whole string (the last index is true)
        return can_decompose[-1]


s = "apple"
dictionary = ["ap", "pl", "ppp", "pple"]

print(Solution().canDecompose(dictionary, s))
