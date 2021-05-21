class MyDecorator:

    def __init__(self, function):
        self.function = function

    def __call__(self):
        print("Inside Function Call")
        self.function()


@MyDecorator
def function():
    print("GeeksforGeeks")


def main():
    function()


if __name__ == "__main__":
    main()
