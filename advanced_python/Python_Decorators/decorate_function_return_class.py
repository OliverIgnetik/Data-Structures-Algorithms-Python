class Addition(object):

    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)

    def run(self, *args, **kwargs):
        raise NotImplementedError('Subclass must implement `run`.')

    def identity(self):
        return 'Hi George, I''m here to help you with addition !'


def addition(decorated):
    class AddSubclass(Addition):
        def run(self, *args, **kwargs):

            if args:
                add = 0
                for arg in args:
                    add = arg + add  # add arguments
                return add

            else:
                # func is called if there are no arguments passed.
                return decorated(*args, **kwargs)

    return AddSubclass()


@addition
def func(*args):
    return 1 + 1


print(func.identity())
print(func())
print(func(2, 2))
print(func(2, 1, 4))
