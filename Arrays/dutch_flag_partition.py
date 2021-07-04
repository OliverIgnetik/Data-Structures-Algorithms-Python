# resource : https://www.youtube.com/watch?v=ER4ivZosqCg

"""
Made famous by Dijkstra
Organizes the array into:

- elements less then the pivot 
- elements equal to the pivot 
- elements greater then the pivot
"""


# Time : O(N^2), Space : O(1)
# Make two passes each which take O(N^2) work
def dutch_flag_partition_1(pivot_index, A):
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


# Time : O(N), Space : O(1)
def dutch_flag_partition_2(pivot_index, A):
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


# Time : O(N), Space : O(1)
def dutch_flag_partition_3(pivot_index, A):
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


arr = [2, 3, 6, 17, 9, 10, 1, 5]

print(dutch_flag_partition_2(4, arr))
