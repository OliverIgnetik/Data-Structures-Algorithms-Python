import random

# Time : O(k), Space : O(1)


def random_sampling(k, A):
    for i in range(k):
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
