def powerOfFour(input):
    '''
    :type input: int
    :rtype: bool

    The number 0x55555555 is a 32 bit number with all odd bits set as 1 and all even bits as 0
    We also check if input > 0 and input is power of 2

    '''
    alternatingOddBitMask = 0x55555555  # 0101 0101 0101 0101 0101 0101 0101 0101

    isNonZero = input != 0
    hasSingleLeadingOneBit = (input & (input - 1)) == 0  # ie. power of 2
    # This checks to make sure that the single leading bit is in an odd location ie. 2^0 + 2^2 + 2^4 .....
    hasOnlyOddPositionedBits = (input & alternatingOddBitMask) == input

    return isNonZero and hasSingleLeadingOneBit and hasOnlyOddPositionedBits


from math import log


def powerOfFour_alt(num: int) -> bool:
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
        res = log(num, 4) - int(log(num, 4))
        return (res == 0)
    else:
        return False
