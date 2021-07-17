"""
Every even position bit is swapped with adjacent bit on right side
, and every odd position bit is swapped with adjacent on left side.

00010111
00101011

The solution assumes that input number is stored using 32 bits.
"""


def swapBits(x):

    # Get all even bits of x
    even_bits = x & 0xAAAAAAAA

    # Get all odd bits of x
    odd_bits = x & 0x55555555

    # Right shift even bits so they become odd bits
    even_bits >>= 1

    # Left shift odd bits so they become even bits
    odd_bits <<= 1

    # Combine even and odd bits
    return (even_bits | odd_bits)


# Driver program
# 00010111
x = 23

# Output is 43 (00101011)
print(swapBits(x))
