# Exercise 4.1 EPI Parity Check

# O(N) approach
def parity_check_1(n):
    res = 0
    while n:
        res ^= n & 1
        n >>= 1
    return res


"""
Bit flip trick
n & (n-1) equals n with the LSB set to zero
eg. n = (00101100) and n - 1 = (00101011)
n & (n-1) = (00101000)
"""


def parity_check_2(n):
    result = 0
    while n:
        result ^= 1
        n &= n - 1  # drops the lowest bit of n
    return result


# O(logN)
def parity_check_3(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


print(parity_check_1(11))
print(parity_check_2(11))
print(parity_check_3(11))
