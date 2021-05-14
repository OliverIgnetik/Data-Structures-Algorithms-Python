from nose.tools import assert_equal


def reverse(word):
    size = len(word)
    if size == 0:
        return
    last_char = word[size-1]
    print(last_char, end='')
    return reverse(word[0:size-1])


def reverse_alt(word):
    size = len(word)
    if size == 0:
        return ''
    last_char = word[size-1]
    return last_char + reverse_alt(word[0:size-1])


class TestReverse(object):

    def test_rev(self, solution):
        assert_equal(solution('hello'), 'olleh')
        assert_equal(solution('hello world'), 'dlrow olleh')
        assert_equal(solution('123456789'), '987654321')

        print('PASSED ALL TEST CASES!')


# Run Tests
# test = TestReverse()
# test.test_rev(reverse_alt)

print(reverse_alt('hello there'))
print(reverse('hello there'))
