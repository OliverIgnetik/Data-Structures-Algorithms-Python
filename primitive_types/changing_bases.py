# NOTES ON BASES
"""
Reference : https://www.mathsisfun.com/numbers/bases.html

Bases
----
Binary : 01 (2)
Ternary : 012 (3)
Quarternary : 0123 (4)
.
.
.
.
Decimal : 0123456789 (10)
Hexadecimal : 0123456789abcdef (16)
Hexatridecimal : 0123456789abcdef.....z (36)
Sexagesimal (60)

Examples
----
Input : ("123", 4, 16)
Output : "1B"

Convert to decimal from quartenary
3*4^0 + 2*4^1 + 1*4^2 = 27

Convert to hexadecimal 
27%16 = 11 -> B
1%16 = 1 -> 1
"""


class Solution:
    def old_bases_to_decimal(self, s: str, b1: int) -> int:

        num = 0
        power = 0
        for i in range(len(s) - 1, -1, -1):
            if self.is_number(s[i]):
                weight = int(s[i])
            else:
                temp = s[i].capitalize()
                weight = (ord(temp) - ord('A') + 1) + 9
                if weight > b1 - 1:
                    raise ValueError(f'Invalid input for base {b1}')

            num += weight * b1**power
            power += 1
        return num

    def decimal_to_new_bases(self, num: int, b2: int) -> str:
        s = ''
        # keep dividing until we get to zero
        # MSB goes at the front
        while num > 0:
            s = self.to_ascii(num % b2) + s
            num //= b2

        return s

    def to_ascii(self, num: int) -> str:
        if num > 9:
            c = chr(ord('A') - 1 + (num - 9))
        else:
            c = str(num)
        return c

    def is_number(self, x: str) -> bool:
        try:
            float(x)
            return True
        except ValueError:
            pass
        return False

    def change_bases(self, s: str, b1: int, b2: int) -> str:
        """"
        input
        ----
        s : integer represented as a string in base b1
        b1 : base 1
        b2 : base 2

        output
        ----
        res : output string

        Complexity
        Time : O(s)
        Space : O(1)
        """
        if b1 not in range(2, 37) or b2 not in range(2, 37):
            raise ValueError('Please input a base between 2 and 36 inclusive')
        num = self.old_bases_to_decimal(s, b1)
        res = self.decimal_to_new_bases(num, b2)
        return res


sol = Solution()
print(sol.old_bases_to_decimal('F', 16))
print(sol.decimal_to_new_bases(27, 16))
print(sol.change_bases('17', 10, 2))
