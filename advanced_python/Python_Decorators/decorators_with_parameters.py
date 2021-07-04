# Python code to illustrate
# Decorators with parameters in Python

def decorator_func(x, y):

    def Inner(func):

        def wrapper(*args, **kwargs):
            print("I like Geeksforgeeks")
            print("Summation of values - {}".format(x + y))

            func(*args, **kwargs)

        return wrapper
    return Inner


# Not using decorator
def my_fun(*args):
    for ele in args:
        print(ele)


# another way of using dacorators
decorator_func(12, 15)(my_fun)('Geeks', 'for', 'Geeks')
print('-' * 60)


# Python code to illustrate
# Decorators with parameters in Python (Multi-level Decorators)
def decodecorator(dataType, message1, message2):
    def decorator(fun):
        print(message1)

        def wrapper(*args, **kwargs):
            print(message2)
            if all([type(arg) == dataType for arg in args]):
                return fun(*args, **kwargs)
            return "Invalid Input"
        return wrapper
    return decorator


@decodecorator(str, "Decorator for 'stringJoin'", "stringJoin started ...")
def stringJoin(*args):
    st = ''
    for i in args:
        st += i
    return st


@decodecorator(int, "Decorator for 'summation'\n", "summation started ...")
def summation(*args):
    summ = 0
    for arg in args:
        summ += arg
    return summ


print(stringJoin("I ", "like ", "Geeks", "for", "geeks"))
print()
print(summation(19, 2, 8, 533, 67, 981, 119))
