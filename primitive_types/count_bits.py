"""
Counts the number of bits set to 1 in a number
O(N) where N is the number of bits
"""


def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        # shift the bits to the right
        x >>= 1
    return num_bits


print(count_bits(17))
