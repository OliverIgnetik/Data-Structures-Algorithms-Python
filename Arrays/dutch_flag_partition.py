# resource : https://www.youtube.com/watch?v=ER4ivZosqCg

"""
Made famous by Dijkstra
Organizes the array into:

- elements less then the pivot
- elements equal to the pivot
- elements greater then the pivot
"""

# Make two passes each which take O(N^2) work


def dutch_flag_partition_1(pivot_index, A):
    """
    Complexity 
    Time : O(N^2)
    Space : O(1)
    """
    pivot = A[pivot_index]

    # group elements smaller than the pivot
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break

    # group elements larger than the pivot
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break

        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break

    return A


def dutch_flag_partition_2(pivot_index, A):
    """
    Complexity 
    Time : O(N)
    Space : O(1)
    """
    pivot = A[pivot_index]
    # use the smaller index to throw elements that are less then the pivot back
    # to the correct place in the array
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1

    larger = len(A) - 1

    for i in reversed(range(len(A))):
        # if we reach this point then we are finished
        if A[i] < pivot:
            break
        # use the larger index to throw elements that are greater then the pivot forward in the array
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1

    return A


def dutch_flag_partition_3(pivot_index, A):
    """
    Makes use of three pointers
    This syntax is not that clear

    Complexity
    Time : O(N)
    Space : O(1)
    """
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)

    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]

    return A


def dutch_flag_partition_4(pivot_index, A):
    """
    This is similar to approach 3 but the syntax is more readable 

    Complexity 
    Time : O(N)
    Space : O(1)
    """
    i, l, r = 0, 0, len(A) - 1
    # everything to the right of r is greater then the pivot
    # everything to the left of l is less then the pivot
    # everything in between is equal to the pivot

    pivot = A[pivot_index]
    # we only need to check up to r because everything behind r is already where it should be
    while i <= r:
        if A[i] > pivot:
            # move element to end of the Array
            A[i], A[r] = A[r], A[i]
            # r got what it wanted so decrement
            r -= 1
        elif A[i] < pivot and i > l:
            # move element to the beginning of the Array
            A[i], A[l] = A[l], A[i]
            # l got what it wanted so increment
            l += 1
        else:
            # this is the pivot continue on
            i += 1
    return A


arr = [2, 3, 6, 17, 9, 10, 1, 5]

print(dutch_flag_partition_4(4, arr))
