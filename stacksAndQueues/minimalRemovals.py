"""
Minimum Removals for Valid String
Given a string s consisting of lowercase letters (a-z) as well as opening ( and closing parenthesis ), remove a minimal number of opening or closing parentheses so that the resulting string is valid.

We say that a string s is valid provided that at least one of the following three conditions hold:
1.) Base Case: s is the empty string, or s does not contain any opening or closing parentheses.
2.) Recursive Rule: s can be written in the form AB (which denotes the string A concatenated with the string B) where A and B are both valid strings.
3.) Recursive Rule: s can be written in the form (A) (which denotes an opening parenthesis ( followed by the string A followed by a closing parenthesis )), where A is a valid string.

Example 1:
Input: "a)b(c)d"
Output: "ab(c)d"
Explanation: We removed the first ")" parenthesis since it created a string that wouldn't be parsable. A potential tree to show how we can parse the min-removal answer is:

                "ab(c)d"
            /             \
     "ab" (rule 1)   "(c)d" (rule 2)
                        /         \
                "(c)" (rule 3)  "d" (rule 1)
                    /
            "c" (rule 1)
"""


class Solution:
    def makeStringValid(self, s):
        """
        Interface
        ----
        :type s: str
        :rtype: str

        Approach 
        ----
        1. The approach is to simply remove all of the parentheses that do not have a matching pair.
        It is clear that this is optimal since removing fewer parentheses would result in at least one unmatched pair,
        and our string would not be valid as per our definition. 

        2. Furthermore, one can see that removing all unmatched parentheses will necessarily match our definition of a string being valid.
        From here, the main problem reduces to determining which parentheses in our string are unmatched. 

        3. In order to determine whether or not each opening parentheses has a corresponding closing parenthesis (and vice-versa),
        we can use the stack data structure to pair the most recent opening parentheses to any closing parentheses that we encounter.

        4. More precisely, we can push the opening parentheses that we encounter onto a stack and pop one from the stack when we encounter 
        closing parentheses (this simulates the pairing process). 

        5. If the stack is empty when we encounter a closing parenthesis, we cannot pair the closing parentheses to an opening one.
        Hence, we must remove this closing parenthesis. 

        6. Conversely, if the stack is non-empty after processing the entire string, the opening parentheses on the stack cannot be paired to closing
        parentheses, so they must be removed.


        7. For implementation purposes, we can maintain a boolean array whose size is equal to the inputted string's size. 
        The value at each index will be set to true if we must remove the character at the index and false otherwise. 

        8. Furthermore, of pushing the actual opening parentheses onto the stack, we can instead push the index at which
        the opening parenthesis was encountered for indexing purposes.

        Complexity
        ----
        Time : O(N)
        Space : O(N)
        """

        # Convert string to list
        # As string is immutable DS in Python
        s = list(s)
        stack = []
        for i, char in enumerate(s):

            # Add index of Open paranthesis in stack
            if char == '(':
                # add the index
                stack.append(i)
            # Case of Close Paranthesis
            elif char == ')':
                # If stack is not empty pop the stack
                if stack:
                    stack.pop()
                # Else we have to remove that close parenthesis from the list
                # because it is invalid
                else:
                    s[i] = ''
        # Remove the open paranthesis from stack whose indices are present in the stack
        while stack:
            # these unmatched parenthesis are invalid
            s[stack.pop()] = ''
        return ''.join(s)


i = "a)b(c)d"
s = Solution()
print(s.makeStringValid(i))
