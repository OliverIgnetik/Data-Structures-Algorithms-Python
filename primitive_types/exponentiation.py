# we get more work done with fewer multiplications to accomplish the same result
"""
x^(1010) = x^[(101)+(101)] = x^(101) x^(101)

x^(101) = x^[(100)+(1)] = x^(10) x^(10) x
"""


def power(x, y):
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result


print(power(2, 3))
