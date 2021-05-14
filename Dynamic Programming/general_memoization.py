from nose.tools import assert_equal


def memoize(f):
    mem = {}

    def decorated_function(num):
        if num not in mem:
            mem[num] = f(num)
        return mem[num]

    return decorated_function


@memoize
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


print(fib(4))


class TestFib(object):

    def test(self, solution):
        assert_equal(solution(10), 55)
        assert_equal(solution(1), 1)
        assert_equal(solution(23), 28657)
        print('Passed all tests.')


# UNCOMMENT FOR CORRESPONDING FUNCTION
t = TestFib()

t.test(fib)
