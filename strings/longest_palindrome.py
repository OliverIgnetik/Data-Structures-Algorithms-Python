"""
Example 1
Input: "aabbc"
Output: 5 
Explanation: The longest palindromes possible are {"abcba", "bacab"}

Example 2
Input: "abbcccd"
Output: 5
Explanation: The original string length is 7, but the longest palindromes are {"cbcbc",  "bcccb"}; 'a' and 'd' were not used.

Example 3
Input: "xyz"
Output: 1


Approaches
----
Count even frequency of characters. The only place that an odd frequency character can 
occur is the middle.

eg. 'abcbaabbdeeeee'

a - 4
b - 4
c - 1 (can only occur in the middle)
d - 1 (can only occur in the middle)
e - 5 (highest frequency odd number)

The highest frequency odd number is very important. This is what can be sandwhiched in 
between the even frequency elements.

eg. aabb bbaa
- we can sandwhich 5 es in here and still have a palindrome
"""


class HashSolution:
    def longest_palindrome(self, s: str) -> int:
        """
        Complexity
        ----
        Time : O(N)
        Space : O(N)
        """
        d = {}
        # count occurences of letters
        for l in s:
            if l in d:
                d[l] += 1
            else:
                d[l] = 1

        # We need to find the letter with the highest odd frequency to sandwhich in the middle
        # and we need to add all the contributions of even frequency letters
        palindrome_length = 0
        highest_odd_occurence_value = 0
        highest_odd_occurence_key = ''
        for key, value in d.items():
            # even letter so add to length
            if value % 2 == 0:
                palindrome_length += value
            else:
                # keeping track of the highest odd occurence
                if value > highest_odd_occurence_value:
                    highest_odd_occurence_key = key
                    highest_odd_occurence_value = value

        # add the highest_odd_occurence_value
        palindrome_length += highest_odd_occurence_value

        # add the leftover odd frequency letters
        for key, value in d.items():
            if value % 2 != 0 and key != highest_odd_occurence_key:
                palindrome_length += value - 1

        return palindrome_length


class SetSolution:
    def longestPalindrome(self, s: str) -> int:
        """
        Complexity
        ----
        Time : O(N)
        Space : O(N)
        """
        # unmatched characters
        unmatched_chars = set()
        count = 0
        for let in s:
            # we have seen it before
            if let in unmatched_chars:
                unmatched_chars.remove(let)
                count += 2
            # we have not seen it before
            else:
                unmatched_chars.add(let)

        # we can only add one more unmatched letter
        if len(unmatched_chars) != 0:
            count += 1

        return count


print(HashSolution().longest_palindrome("abbcccd"))
print(SetSolution().longestPalindrome("abbcccd"))
