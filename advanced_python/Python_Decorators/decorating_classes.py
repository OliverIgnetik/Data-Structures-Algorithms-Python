class MyDecorator:

    def __init__(self, function):
        self.function = function

    def __call__(self):
        print("Inside __call__ of", self.function.__name__)
        self.function()


@MyDecorator
def simple_function():
    print("GeeksforGeeks")


def main():
    simple_function()


if __name__ == "__main__":
    main()
