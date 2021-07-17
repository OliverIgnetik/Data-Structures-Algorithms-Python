from math import log10, floor


def isPalindrome_constant_space(num: int) -> bool:
    """
    Complexity 
    Time : O(N) we only look at each digit once
    Space : O(1)
    """
    if num < 0:
        return False

    # log10 asks how many times can we divide by 10?
    total_num_digits = int(floor(log10(num))) + 1
    mask = int(pow(10, total_num_digits - 1))  # mask
    for _ in range(total_num_digits // 2):
        most_significant_digit = num // mask  # most significant digit
        least_signficant_digit = num % 10  # least significant digit

        if most_significant_digit != least_signficant_digit:
            return False

        num %= mask  # remove most signficant digit
        num //= 10  # remove least significant digit
        mask //= 100  # remove two 0's from the mask

    return True


print(isPalindrome_constant_space(9232))
