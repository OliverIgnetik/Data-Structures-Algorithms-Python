# PYTHON BITWISE OPERATORS
"""
&   a & b   Bitwise AND
| 	a | b 	Bitwise OR
^	a ^ b	Bitwise XOR (exclusive OR)
~	~a	    Bitwise NOT
<<	a << n	Bitwise left shift
>>	a >> n	Bitwise right shift
"""


def reverse_bits(num: int) -> int:
    """
    We must reverse the significant bits of a numberself.
    We ignore the leading zeros and num >= 0.

    input
    ----
    num : int

    output 
    ----
    res : int

    Examples
    input : 1011 (1 + 2 + 8 = 11)
    output : 1101 (1 + 4 + 8 = 13)

    Complexity 
    Time : O(N)
    Space : O(1)
    """
    output = 0

    while num != 0:
        # shift output to the left
        output <<= 1

        # check if the LSB is 1
        if num & 1 == 1:
            # if it is add 1 to output (ie. bitwise OR)
            output |= 1

        # now move on to next bit (ie. bitwise shift to the right)
        num >>= 1

    return output
