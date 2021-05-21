from nose.tools import assert_equal


# pythonic answer
def uni_char(s):
    return len(set(s)) == len(s)


# set answer O(N) time complexity
# O(K) space complexity where K is the number of items in the set

def uni_char2(s):
    chars = set()
    for let in s:
        # Check if in set
        if let in chars:
            return False
        else:
            # it will only add the letter once
            chars.add(let)
    return True


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')


# Run Tests
t = TestUnique()
t.test(uni_char)
