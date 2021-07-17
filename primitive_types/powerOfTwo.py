from math import log2


def powerOfTwo(num: int) -> bool:
    """
    We need to find if num is a power of two?

    Complexity 
    Time : O(1)
    Space : O(1)

    Explanation 
    log2(8) = 3.0
    log2(16) = 4.0

    We should expect the log_2 to be a whole number
    So the difference between the result cast as an int 
    and the result as a float should be the same
    """
    if num > 0:
        res = log2(num) - int(log2(num))
        return (res == 0)
    else:
        return False


def powerOfTwo_alternative(num: int) -> bool:
    """
    If the number is a power of two only one bit will be set to 1
    Complexity 
    Time : O(1)
    Space : O(1)

    Explanation 
    1. 
    num = 6 (1100)
    num - 1 = 5 (0101)
    num & (num - 1) = 0100
    2. 
    num = 8 (1000)
    num - 1 = 7 (0111)
    num & (num - 1) = 0000
    """
    return num > 0 and (num & (num - 1)) == 0


from math import log


def powerOfBase(num: int, base: int) -> bool:
    if (num > 0 and (log(num, 4) - int(log(num, 4)) == 0)):
        return True
    else:
        return False


print(powerOfTwo(17))
print(powerOfBase(64, 4))
