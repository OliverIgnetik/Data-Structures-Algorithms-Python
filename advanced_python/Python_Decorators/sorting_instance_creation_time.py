import functools
import time

# when we wrap a class with a decorator we need to provide a class as an input


def sort_by_creation_time(cl):
    org_init = cl.__init__

    # Enhance the class to store the creation
    # time based on the instantiation.
    @functools.wraps(org_init)
    def new_init(self, *args, **kwargs):
        org_init(self, *args, **kwargs)
        self._created = time.time()

    # set the init of the decorated class to the function defined above
    cl.__init__ = new_init
    # __lt__ and __gt__ are overloaded comparison operators
    cl.__lt__ = lambda self, other: self._created < other._created
    cl.__gt__ = lambda self, other: self._created > other._created
    return cl


@sort_by_creation_time
class Sort:
    def __init__(self, identifier):
        self.identifier = identifier

    def __repr__(self):
        return self.identifier


def main():

    first = Sort('Python')
    second = Sort('Data Analysis')
    third = Sort('Machine Learning')

    sortables = [third, first, second]
    print(sorted(sortables))


if __name__ == "__main__":
    main()
