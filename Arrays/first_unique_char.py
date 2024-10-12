from typing import Tuple

def first_unique_chars(myStr: str) -> Tuple[int, str]:
    chars = {}
    for i, x in enumerate(myStr):
        if x not in chars:
            chars[x] = i
        else:
            chars[x] = -1

    for char in chars:
        if chars[char] != -1:
            return (chars[char], char)

    raise ValueError("There are no unique chars")


myStr = 'hhelleoo'
print(first_unique_chars(myStr))
