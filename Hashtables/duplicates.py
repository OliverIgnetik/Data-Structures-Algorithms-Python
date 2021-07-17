from typing import List


def duplicates(arr: List[int]) -> List[int]:
    d = {}
    duplicates = []
    for x in arr:
        if x not in d:
            d[x] = 1
        elif d[x] == 1:
            d[x] += 1
            duplicates.append(x)
        else:
            continue
    return duplicates


print(duplicates([1, 1, 2, 2]))
