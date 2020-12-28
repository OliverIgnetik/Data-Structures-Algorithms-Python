# Find the squareroot of a given number rounded down to the nearest integer

# The squareroot of a number N always lies between 0 and N/2

def solution(num):
    if num < 0:
        raise ValueError
    if num == 1:
        return 1
    # range(N) goes from 0 to N-1
    # thus you need to use num//2 + 1

    for k in range(1+(num//2)):
        if k**2 == num:
            return k
        elif k**2 > num:
            return k-1
    return k

# Binary search increases efficiency to log(N/2)
# where N is the integer


def better_solution(num):
    if num < 0:
        raise ValueError
    if num == 1:
        return 1
    low = 0
    high = 1+(num//2)

    while low+1 < high:
        mid = low+(high-low)//2
        square = mid**2
        if square == num:
            return mid
        elif square < num:
            low = mid
        else:
            high = mid

    return low


print(solution(14))
print(better_solution(14))
