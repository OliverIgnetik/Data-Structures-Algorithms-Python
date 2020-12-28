def solution(lst, target):

    # Create set to keep track of duplicates
    seen = set()

    # We want to find if there is a num2 that sums with num to reach the target

    for num in lst:

        num2 = target - num

        if num2 in seen:
            return True

        seen.add(num)

    # If we never find a pair match which creates the sum
    return False


print(solution([1, 2, 3, 4, 5], 6))
