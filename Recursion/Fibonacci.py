def fib(num):
    a = 0
    b = 1
    sum_ = 0
    for i in range(0, num):
        sum_ = a+b
        a = b
        b = sum_
    return sum_

# time complexity - O(2^N)


def fibonacci(num):
    if num < 2:
        return num
    return fib(num-1) + fib(num-2)


print(fib(5))
print(fibonacci(5))
