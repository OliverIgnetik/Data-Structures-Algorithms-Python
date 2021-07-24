"""
Phone Number Mnemonics
Given a string digits representing a phone number, return all possible character arrangements that can result from the number.

Each digit maps like so:
2 -> "a" | | "b" | | "c"
3 -> "d" | | "e" | | "f"
4 -> "g" | | "h" | | "i"
5 -> "j" | | "k" | | "l"
6 -> "m" | | "n" | | "o"
7 -> "p" | | "q" | | "r" | | "s"
8 -> "t" | | "u" | | "v"
9 -> "w" | | "x" | | "y" | | "z"

Example 1:
Input: "43"
Output: ["gd", "ge", "gf", "hd", "he", "hf", "id", "ie", "if"]

Example 2:
Input: "239"
Output:
[
    "adw", "adx", "ady", "adz",
    "aew", "aex", "aey", "aez",
    "afw", "afx", "afy", "afz",
    "bdw", "bdx", "bdy", "bdz",
    "bew", "bex", "bey", "bez",
    "bfw", "bfx", "bfy", "bfz",
    "cdw", "cdx", "cdy", "cdz",
    "cew", "cex", "cey", "cez",
    "cfw", "cfx", "cfy", "cfz"
]

Constraints:
s will only digits between 2 and 9
2 <= n <= 10 (constraint on length of string)
"""
from typing import List


class Solution:

    # This can be a hashtable, any structure to map 'number' to 'letters' it can manifest as
    digit_to_possible_letters = [
        "",      # 0
        "",      # 1
        "abc",   # 2
        "def",   # 3
        "ghi",   # 4
        "jkl",   # 5
        "mno",   # 6
        "pqrs",  # 7
        "tuv",   # 8
        "wxyz"   # 9
    ]

    def letterCombinations(self, digits: str) -> List[str]:
        """
        Interface
        ----
        :type digits: str
        :rtype: list of str

        Approach 
        ----
        1. Identify the decision space at every recursive stack frame
        NOTE: we are deciding on which letter at each slot

        2. Model the recursive calls, constraints, state and goal
        NOTE: state includes the data that exists in each stack frame 
        1. the digit number (current index of str of numbers)
        2. the placed items (partialString)
        3. answer list (mnemonics)
        4. mapping of digit to chars

        NOTE: GOAL 
        - we reach the goal when we see that the current digit is the same as the total number of digits in the input

        NOTE: CONSTRAINT 
        - is based on the mappings and the length of digits

        3. Identify when to backtrack
        NOTE: when we return to the stack frame we have to backtrack on out placing to make the next choice

        Complexity
        ----
        Recurrence Relation 
        T(N) <= 4T(N-1) + O(1)

        Because we are doing constant work at each stack frame 
        we can upper bound to the amount of calls 
        Branching factor = 4 
        NOTE: we could have derived this using the recurrence relation

        Time : O(4^N) the recursion tree can go N levels deep
        Space : O(N) the call stack can go N levels deep
        """

        #  When input string is empty
        if len(digits) == 0:
            return []

        mnemonics = []
        self.explore_combinations(0, "", digits, mnemonics)

        return mnemonics

    # Helper function for recursively calculating the ans
    def explore_combinations(self, current_digit: int, partial_mnemonic: str, digits: str, mnemonics: List[str]) -> None:

        # Base Case - We have got an answer return back to the caller
        if current_digit == len(digits):
            mnemonics.append(partial_mnemonic)
            return

        digit_character = digits[current_digit]
        digit_as_int = int(digit_character)

        letters = Solution.digit_to_possible_letters[digit_as_int]

        # O(1) ie. there can be max four letters
        for possible_letter in letters:
            # 1.) Choose - Append the letter that this digit can materialize into
            partial_mnemonic = partial_mnemonic + possible_letter

            # 2.) Explore - Recurse on the decision with changed state. We advance the digit we are working on.
            self.explore_combinations(
                current_digit + 1, partial_mnemonic, digits, mnemonics)

            # 3.) Unchoose - We have returned to this stack frame of choice. Remove the choice, next loop will choose again.
            partial_mnemonic = partial_mnemonic[:-1]


nums = "239"
s = Solution()
print(s.letterCombinations(nums))
