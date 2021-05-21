def reverse_decorator(function):

    def reverse_wrapper():
        make_reverse = "".join(reversed(function()))
        return make_reverse

    return reverse_wrapper


def uppercase_decorator(function):

    def uppercase_wrapper():
        var_uppercase = function().upper()
        return var_uppercase

    return uppercase_wrapper


@uppercase_decorator
@reverse_decorator
def say_hi():
    return 'hi george'


def main():
    print(say_hi())


if __name__ == "__main__":
    main()
