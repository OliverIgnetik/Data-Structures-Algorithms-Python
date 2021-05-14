from functools import lru_cache
import time


def add80(n):
    time.sleep(1)
    print('loading...')
    return n+80


print(add80(5))
print(add80(5))

# Memoization 1

cache = {}


def memoizedadd80(n):
    if n in cache:
        return cache[n]
    else:
        time.sleep(1)
        print('loading...')
        cache[n] = n+80
        return cache[n]


print(memoizedadd80(6))
print(memoizedadd80(6))


# Memoization 2
# Use of higher order function and lexical closure
# the returned function remembers the state of the enclosing function

def memoizedadd80():
    cache = {}

    def memoized(n):
        if n in cache:
            return cache[n]
        else:
            time.sleep(1)
            print('loading...')
            cache[n] = n + 80
            return cache[n]
    return memoized


memo = memoizedadd80()
print(memo(7))
print(memo(7))


# https://docs.python.org/3.3/library/functools.html --> Doc for lru_cache

# Memoization 3 LRU cache
@lru_cache(maxsize=1000)
def memoized2add80(n):
    return n + 80


print(memoized2add80(8))
print(memoized2add80(8))
print(memoized2add80.cache_info())
