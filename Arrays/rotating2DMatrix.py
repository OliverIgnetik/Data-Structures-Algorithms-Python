class Solution:
    def rotate(self, A):
        """
        Complexity
        Time : O()
        Space : O(1) no auxilary data structures used in this solution
        """
        N = len(A)
        i = 0
        j = N - 1
        # flip rows about middle row
        while i < N // 2:
            k = 0
            while k < N:
                A[i][k], A[j][k] = A[j][k], A[i][k]
                k += 1
            i += 1
            j -= 1

        # do transpose - reflect along diagonal
        for i in range(N):
            for j in range(i, N):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        return A


A1 = [
    [10, 20],
    [30, 40]
]

A2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(Solution().rotate(A1))
print(Solution().rotate(A2))
