from nose.tools import assert_equal

################ Problem Definition #####################################

# Given an integer array, output all the **unique** pairs that sum up to a specific value **k**.

# So the input:

#     pair_sum([1,3,2,2],4)

# would return **2** pairs:

#      (1,3)
#      (2,2)

################ Solution #####################################


# pythonic solution

def anagram(s1, s2):
    # remove and make lower
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)  # O(NlogN)


def anagram2(s1, s2):

    s1 = s1.replace(' ', '').lower()  # O(N)
    s2 = s2.replace(' ', '').lower()  # O(N)

    # edge case check
    if len(s1) != len(s2):  # O(1)
        return False

    count = {}

    # add letters to count
    for letter in s1:  # O(N)
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    # subtract letters from count
    for letter in s2:  # O(N)
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    # if the count is not zero then it must not be an anagram
    for letter in count:  # O(N) overall time complexity
        if count[letter] != 0:
            return False

    return True


# rudimentary tests for anagram using nose.tools.assert_equal
class AnagramTest(object):

    def test(self, sol):
        assert_equal(sol('go go go', 'gggooo'), True)
        assert_equal(sol('abc', 'cba'), True)
        assert_equal(sol('hi man', 'hi     man'), True)
        assert_equal(sol('aabbcc', 'aabbc'), False)
        assert_equal(sol('123', '1 2'), False)
        print("ALL TEST CASES PASSED")


print(anagram('clint eastwood', 'old west action'))

# Run Tests
# t = AnagramTest()
# t.test(anagram)
# t.test(anagram2)
