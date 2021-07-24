from typing import List
from itertools import combinations
from functools import reduce
"""
DIFFERENCE BETWEEN PERMUTATIONS AND COMBINATIONS
permutations('ABCD', 2) AB AC AD BA BC BD CA CB CD DA DB DC NOTE: ORDER MATTERS AD != DA
combinations('ABCD', 2) AB AC AD BC BD CD NOTE: ORDER DOES NOT MATTER AD = DA

NOTE: N Choose R 
Combinations = N!/(R!(N - R)!) ORDER DOES NOT MATTER
Permutations = N!/(N-R)! ORDER MATTERS 
"""


class Solution:
    def two_sum(self, target, i, arr):
        """
        Runs in linear time 
        Scan from (i+1)th index to end of the array
        """
        seen = set()
        output = set()

        for j in range(i + 1, len(arr)):
            num = arr[j]
            complement = target - num
            # If we haven't seen the complement off this num add the complement to seen
            if num not in seen:
                seen.add(complement)
            else:
                # We have seen the complement of this number before so add the pair
                # so we have the numbers ordered properly
                output.add((min(num, complement), max(num, complement)))
        return output

    def three_sum_alternative(self, arr: List[int]) -> List[int]:
        """
        This approach is more optimal because we prevent recomputation

        NOTE: Remember lists are not hashable but tuples are 

        Complexity
        Time : O(N^2)
        Space : O(|N|) We have a seen set
        """
        # we can assume that this takes O(Nk) ie. radix sort
        arr.sort()
        triplets = {}
        for root_index in range(len(arr) - 1):
            root_element = arr[root_index]
            # we want to find a two sum that sums to the -ve value of the current root element
            pairs = self.two_sum(-root_element, root_index, arr)
            # now we have to go through the pairs we have found and make sure we don't add duplicates
            for pair in pairs:
                triplet = (root_element,)
                triplet += pair
                # tuplets are hashable lists are not
                if triplet not in triplets:
                    triplets[triplet] = list(triplet)
        return list(triplets.values())


class SolutionPointers:
    def three_sum(self, A):
        '''
        This approach uses two pointers in the seen two sum and takes advantage of the
        fact that the array is sorted. 

        NOTE: the use of the reducer to turn the list into a string for hashing in the dictionary 

        Complexity 
        Time : O(N^2)
        Space : O(|N|)

        :type A: list of int
        :rtype: list of list of int
        '''
        # Initially sorting is required O(Nk) ie. radix sort
        A.sort()

        # make a set to avoid duplicate
        seen = set()
        # This will store the answer
        all_three_sums = []
        second_to_last_index = len(A) - 2

        for i in range(0, second_to_last_index):
            self.find_two_sum(i, A, all_three_sums, seen)

        return all_three_sums

    def find_two_sum(self, root_index, A, all_three_sums, seen):
        left = root_index + 1
        right = len(A) - 1
        # loop till left => right
        while left < right:
            three_number_sum = A[root_index] + A[left] + A[right]
            # Case when an answer is found
            if three_number_sum == 0:
                number_list = [A[root_index], A[left], A[right]]
                number_list.sort()
                # turn number list into a string
                signature = reduce(lambda acc, num: str(
                    acc) + str(num), number_list)

                if signature not in seen:
                    all_three_sums.append([A[root_index], A[left], A[right]])
                    seen.add(signature)
                # if ans exist than increase left index as well as decrease right index
                left += 1
                right -= 1
            # undershoot so left needs a bigger integer
            elif three_number_sum < 0:  # if sum < 0 only increase left index to get larger sum
                left += 1
            # overshoot so right needs a smaller integer
            else:
                right -= 1  # if sum > 0 only decrease right index to get lesser sum


class IterToolsSolution:
    def three_sum_itertools_approach(self, arr: List[int]) -> List[List[int]]:
        """
        Given an array of integers return all the unique triplets that sum to 0
        input
        ----
        arr : list of integers
        NOTE: this means sorting array can be down in O(N + k) using radix sort

        output
        ----
        res : list of lists of integers
        NOTE: Duplicate triplets are not allowed in the output

        Complexity
        Time : O(N Choose R) 
        Space : O(N Choose R) 
        """
        res = {}
        unique_triplets = list(combinations(arr, 3))
        for triplet in unique_triplets:
            sorted_triplet = tuple(sorted(triplet))
            if sum(sorted_triplet) == 0 and sorted_triplet not in res:
                res[sorted_triplet] = list(sorted_triplet)

        return res.values()


print(SolutionPointers().three_sum(
    [-5, 3, 2, 0, 1, -1, -5, 3, 2]))
