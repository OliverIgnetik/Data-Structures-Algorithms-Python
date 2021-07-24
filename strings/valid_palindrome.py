class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Complexity
        ----
        Time : O(N) including 
        Space : O(1)
        """
        s = ''.join(s.lower().split(' '))
        # convert to alphanum
        res = ''
        for char in s:
            if char.isalnum():
                res += char

        i, j = 0, len(res) - 1
        while i <= j:
            if res[i] != res[j]:
                return False
            i += 1
            j -= 1

        return True


print(Solution().validPalindrome("a, b, c, ba"))
