def frog_jump(k):
    """
    Recursive function for solving frog jump problem 
    input: number of stones
    output: number of ways
    """
    nums = [0] * (k + 1)
    if k == 1:
        return 1
    if k == 2:
        return 2
    nums[1], nums[2] = 1, 2
    for i in range(3, k + 1):
        nums[i] = nums[i - 1] + nums[i - 2]
    return nums[k]


print(frog_jump(10))
