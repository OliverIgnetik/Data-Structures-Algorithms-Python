##################### Problem ######################

# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

# The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

##################### Solution #####################

from nose.tools import assert_equal


def compress(s):
    """
    This solution compresses without checking. Known as the RunLength Compression algorithm.
    """

    # Begin Run as empty string
    r = ""
    l = len(s)

    # Check for length 0
    if l == 0:
        return ""

    # Check for length 1
    if l == 1:
        return s + "1"

    # Intialize Values
    last = s[0]
    cnt = 1
    i = 1

    while i < l:
        last = s[i - 1]
        # Check to see if it is the same letter
        if s[i] == last:
            # Add a count if same as previous
            cnt += 1
        else:
            # Otherwise store the previous data
            r = r + last + str(cnt)
            # reset count
            cnt = 1

        # Add to i value to terminate while loop
        i += 1

    # Put everything back into run
    r = r + s[i - 1] + str(cnt)

    return r


class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL TEST CASES PASSED')


print(compress('AAAAABBBBCCCCD'))

# Run Tests
# t = TestCompress()
# t.test(compress)
