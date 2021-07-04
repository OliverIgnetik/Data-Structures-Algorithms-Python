def first_unique_chars(myStr):
    chars = {}
    for i, x in enumerate(myStr):
        if x not in chars:
            chars[x] = i
        else:
            chars[x] = -1

    for x in myStr:
        if x != -1:
            return chars[x]

    return -1


myStr = 'helleo'
print(first_unique_chars(myStr))
