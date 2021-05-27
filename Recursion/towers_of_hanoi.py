from typing import TypeVar, Generic, List
T = TypeVar('T')

####################### Resources #######################
# https://www.youtube.com/watch?v=rf6uf3jNjbo
# https://www.youtube.com/watch?v=YstLjLCGmgg

####################### Rules of Towers of Hanoi #######################

# 1. You cannot place a larger disk on a smaller disk
# 2. The disks must be placed in the same order on the target rod


####################### TIPS #######################
# 1. Focus on getting the largest disk to the target rod
# 2. We need to find ways to move the smaller disks to the temporary rod
# so we can move the largest disk to the target rod

# The key is recognizing the recursive nature to the problem
# In the case of 4 disks: we need to move the 3 smaller disks to the
# temporary rod and move the largest disk to the target rod.
# NOTE: we already have the solution for moving the 3 smaller disks to a target rod

# GOAL: move the disks to the target rod
class Stack(Generic[T]):

    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


num_discs: int = 3
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()
for i in range(1, num_discs + 1):
    tower_a.push(i)

# In the first call
# tower a - begin
# tower b - temp
# tower c - end


def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        # move all but the largest disk to the temporary rod
        hanoi(begin, temp, end, n - 1)
        # move the largest disk to the target rod
        hanoi(begin, end, temp, 1)
        # move all the disks on the temporary rod to the target rod
        hanoi(temp, end, begin, n - 1)


if __name__ == "__main__":
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)
