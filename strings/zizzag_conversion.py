"""
Example 1
Input:
s = "YELLOWPINK"
rows = 4

Output: "YPEWILONLK"
Explanation: There are 4 rows in the zigzag formatted string.

Y     P    (row 1: "YP")
E   W I    (row 2: "EWI")
L O   N    (row 3: "LON")
L     K    (row 4: "LK")

Example 2
Input:
s = "REDBLUEBLACK"
rows = 2

Output: "RDLELCEBUBAK"
Explanation: There are 2 rows in the zigzag formatted string.

R D L E L C    (row 1: "RDLELC")
E B U B A K    (row 2: "EBUBAK")

Example 3
Input:
s = "REDBLUEBLACK"
rows = 1

Output: "REDBLUEBLACK"
Explanation:

R E D B L U E B L A C K    (row 1: "REDBLUEBLACK")
"""


class Solution:
    def zigzag(self, s: str, num_rows: int) -> str:
        """
        Complexity
        ----
        Time : O(N)
        Space : O(N)
        """
        if num_rows == 1:
            return s
        res = ''
        rows = [[] for _ in range(num_rows)]

        j, i = 0, 0
        bottom, top = False, True
        while j < len(s):
            let = s[j]
            rows[i].append(let)
            # if we reach the bottom change the guards
            if i == num_rows - 1:
                bottom, top = True, False
            # if we reach the top change the guards
            elif i == 0:
                top, bottom = True, False

            # coming from the bottom
            if bottom and not top:
                i -= 1
            # coming from the top
            elif top and not bottom:
                i += 1

            j += 1

        # extract the information from each row
        for row in rows:
            for let in row:
                res += let
        return res


print(Solution().zigzag('YELLOWPINK', 4))
print(Solution().zigzag("REDBLUEBLACK", 2))
