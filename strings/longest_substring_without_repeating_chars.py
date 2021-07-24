class NaiveSolution:
    def longestUniqueCharacterSubstring(self, s: str) -> int:
        """
        Complexity
        ----
        Time : O(N^2)
        Space : O(1)
        """
        substring_length = 0
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                if len(set(s[i:j])) == len(s[i:j]):
                    substring_length = max(len(s[i:j]), substring_length)
                else:
                    break

        return substring_length


class OptimizedSolution:
    def longestUniqueCharacterSubstring(self, s: str) -> int:
        '''
        :type s: str
        :rtype: int

        NOTE: Overlapping subproblems always is a good candidate for 
        dynamic programming

        Complexity 
        ----
        Space : O(N)
        Time : O(N)
        '''
        # Create an array for mapping the characters
        mapping = {}

        # Initialise the start,end and maximum to 0
        start = 0
        end = 0
        so_far = 0
        # Iterate the string while start is less than the end
        while end < len(s):
            # If the character has already been seen at a position equal to or
            # after start then update start
            if s[end] in mapping and mapping[s[end]] >= start:
                start = mapping[s[end]] + 1
            # otherwise just update map
            mapping[s[end]] = end

            # update biggest so far
            # we add one to include the element we just checked
            # (ie. the element sitting at the pointer end)
            so_far = max(so_far, end + 1 - start)
            # increment end
            end += 1

        return so_far


s = "ABCABADEC"
sol1 = NaiveSolution()
sol2 = OptimizedSolution()
print(sol1.longestUniqueCharacterSubstring(s))
print(sol2.longestUniqueCharacterSubstring(s))
