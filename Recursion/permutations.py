from nose.tools import assert_equal

# Problem Statement

# Given a string, write a function that uses recursion to output a list of all the possible permutations of that string.

# For example, given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

# *Note: If a character is repeated, treat each occurence as distinct, for example an input of 'xxx' would return a list with 6 "versions" of 'xxx'*


# Solution

def permute(s):

    out = []

    # Base Case
    if len(s) == 1:
        out = [s]

    else:
        # For every letter in string
        for i, let in enumerate(s):

            # For every permutation resulting from Step 2 and 3 described above
            for perm in permute(s[:i] + s[i+1:]):
                # Add it to output
                out += [let + perm]

       # use this print statement to inspect the result of permute
       # print(out)

    return out


class TestPerm(object):

    def test(self, solution):

        assert_equal(sorted(solution('abc')), sorted(
            ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        assert_equal(sorted(solution('dog')), sorted(
            ['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']))

        print('All test cases passed.')


# Run Tests
# t = TestPerm()
# t.test(permute)

print(permute('abc'))
