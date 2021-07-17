def addStrings(s1, s2):
    """
    input
    ----
    s1 : str decimal digits
    s2 : str decimal digits
    output
    ----
    res : str decimal digits

    Complexity
    Time : O(s1 + s2)
    Space : O(s1 + s2)
    """
    def do_addition(i, j, overflow):
        """
        Closure means we only have access to addStrings input parameters
        NOTE: we don't have access to res or digit
        """
        num1 = int(s1[i]) if i >= 0 else 0
        num2 = int(s2[j]) if j >= 0 else 0
        sum_ = num1 + num2 + overflow
        digit = sum_ % 10
        overflow = sum_ // 10
        return digit, overflow

    res = ''
    i = len(s1) - 1
    j = len(s2) - 1
    overflow = 0
    while i >= 0 and j >= 0:
        digit, overflow = do_addition(i, j, overflow)
        res = str(digit) + res
        i -= 1
        j -= 1

    while i >= 0:
        digit, overflow = do_addition(i, j, overflow)
        res = str(digit) + res
        i -= 1

    while j >= 0:
        digit, overflow = do_addition(i, j, overflow)
        res = str(digit) + res
        j -= 1

    if overflow != 0:
        res = str(overflow) + res
    return res


print(addStrings("101", "1"))
