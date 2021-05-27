from functools import lru_cache


@lru_cache(maxsize=1000)
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(10))
print(fib.cache_info())


# O(N) time complexity


cache = {}


def fibo(n):
    if n in cache:
        return cache[n]
    elif n < 2:
        cache[n] = n
        return cache[n]
    else:
        cache[n] = fibo(n - 1) + fibo(n - 2)
        return cache[n]


x = fibo(8)
print(cache)
print(x)


def fib_iter(n):

    # Set starting point
    a = 0
    b = 1

    # Follow algorithm
    for i in range(n):

        a, b = b, a + b

    return a


print(fib_iter(3))
