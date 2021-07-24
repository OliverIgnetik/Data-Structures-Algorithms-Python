from typing import List


"""
N = 10
0 1 2 3 4 5 6 7 8 9
[2,3,5,7,9]
"""
from typing import List


class Solution:
    def naive_enumeration(self, n: int) -> List[int]:
        """
        Enumerates all primes up to the number n
        input
        ----
        n : integer

        output
        ----
        res : list of integers 

        Complexity 
        ----
        Time : O(N^3/2)
        Space : O(N)
        """
        # edge case
        if n < 2:
            raise ValueError('Please input a number greater then 2')

        primes = []
        i = 2
        while i < n:
            j = 2
            isPrime = True
            """
            We only need to consider j < sqrt(i) for example if we consider 36 we know that if we consider
            9 it has a factor less then 6 which is 4
            """
            while j * j < i:
                if i % j == 0:
                    isPrime = False
                j += 1
            if isPrime:
                primes.append(i)
            i += 1

    def sieve_eratosthenes(self, n: int) -> List[int]:
        """
        Enumerates all primes up to the number n
        input
        ----
        n : integer

        output
        ----
        res : list of integers 

        Approach 
        If 2 is prime we mark all the multiples of 2 as not prime. We 
        continue on to the next prime number 3 and mark all of its multiples as 
        not prime.

        Complexity 
        ----
        Time : O(Nlog(logN))
        Space : O(N)
        """
        isPrime = []
        for i in range(n):
            isPrime.append(True)

        # we know these are not primes
        isPrime[0] = False
        isPrime[1] = False

        for i in range(n):
            if isPrime[i]:
                j = i + i
                # this will be a harmonic series
                # n/2 + n/3 + n/4 ..... harmonic series
                while j < n:
                    isPrime[j] = False
                    j += i
        primes = []
        for i in range(n):
            if isPrime[i]:
                primes.append(i)

        return primes


print(Solution().sieve_eratosthenes(19))
