# output is passed along and is returned in the final function
def word_split(phrase, list_of_words, output=None):
    '''
    Note: This is a very "python-y" solution.
    '''

    # Checks to see if any output has been initiated.
    if output is None:
        output = []

    # For every word in list
    for word in list_of_words:

        # If the current phrase begins with the word, we have a split point!
        if phrase.startswith(word):

            # Add the word to the output
            output.append(word)

            # Recursively call the split function on the remaining portion of the phrase--- phrase[len(word):]
            # Remember to pass along the output and list of words
            return word_split(phrase[len(word):], list_of_words, output)
    return output


print(word_split('ilovedogsJohn', ['i', 'am', 'a',
                                   'dogs', 'lover', 'love', 'John']))


def sum_func(n):
    # Base case
    if len(str(n)) == 1:
        return n

    # Recursion
    else:
        return n % 10 + sum_func(n // 10)


print(sum_func(4321))
