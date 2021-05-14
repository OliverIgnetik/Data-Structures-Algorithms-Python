from nose.tools import assert_equal


def pair_sum(arr, k):

    # edge case check
    if len(arr) < 2:
        raise ValueError('There are no pairs in an array with length 1')

    # sets for tracking are great for changing quadratic
    # complexity to linear
    seen = set()
    output = set()

    for num in arr:  # O(N)
        complement = k-num
        # you only need to keep track of one number - the difference
        # ensures unique pairs
        if num not in seen:
            seen.add(complement)
        else:
            output.add((min(num, complement), max(num, complement)))
#     print('\n'.join(map(str,list(output))))
    return len(output)


class TestPair(object):

    def test(self, sol):
        assert_equal(
            sol([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
        assert_equal(sol([1, 2, 3, 1], 3), 1)
        assert_equal(sol([1, 3, 2, 2], 4), 2)
        print('ALL TEST CASES PASSED')


arr = [1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1]

print(pair_sum(arr, 3), 3)

# Run basic tests
# t = TestPair()
# t.test(pair_sum)
