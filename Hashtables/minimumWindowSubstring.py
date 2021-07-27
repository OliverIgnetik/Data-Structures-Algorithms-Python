"""
Minimum Window Substring
Given a string corpus and a string target, find the minimum window (contiguous substring) 
which contain all the characters that are found in target.

The time complexity of the solution should be in order of O(n).

NOTE: substring and  sub-sequence are different things

Example 1:
Input: corpus = "donutsandwafflemakemehungry"  target = "flea"

Output: "affle" or "flema" 

Example 2:
Input: corpus = "whoopiepiesmakemyscalegroan"  target = "roam"

Output: "myscalegro"  

Example 3:
Input: corpus = "coffeeteabiscuits"  target = "cake"

Output: ""  
Explanation: since the letter k is not found in the corpus, a minimum window cannot be found.
"""

import sys


class BruteForceSolution:
    def minWindow(self, searchString, t):
        """
        Interface
        ----
        :type searchString: str
        :type t: str
        :rtype: str

        Approach 
        ----
        1. Plant the left pointer and scan the window 

        2. Find all substrings that contain all of the target

        3. Take the smallest

        Complexity
        ----
        M = target string 
        N = length of query string

        Time : O(N^2)
        Space : O(1)
        """
        n = len(searchString)

        # It contains the min length seen so far
        min_window_size = sys.maxsize

        # It contains the minimum length substring
        min_window = ""

        # The nested for loop help us generate all the substrings
        for left in range(0, n):
            for right in range(left, n):

                # Generate the substring
                window_snippet = searchString[left: right + 1]

                # Check if the generated char contains all the characters of target
                window_contains_all = self.contains_all(window_snippet, t)

                # If it is a valid substring
                # And the length is less than the minimum so far
                # Update the answer
                if window_contains_all and len(window_snippet) < min_window_size:
                    min_window_size = len(window_snippet)
                    min_window = window_snippet

        return min_window

    # Helper function to check if all the char of string are
    # Present in the string searchString
    def contains_all(self, searchString, t):
        """
        This is a really convoluted way of doing this 
        1. You could use better syntax 
        2. Or make use of Collections.Counter()
        """
        required_characters = {}

        for i in range(0, len(t)):
            occurrences = 0
            if t[i] in required_characters:
                occurrences = required_characters[t[i]]

            required_characters[t[i]] = occurrences + 1

        for i in range(0, len(searchString)):
            curr = searchString[i]

            if curr in required_characters:
                # Calculate what the new occurrence count will be
                new_occurrences = required_characters[curr] - 1

                """
                If we have satisfied all of the characters for this character, remove the key
                from the hashtable.
                 
                Otherwise, just update the mapping with 1 less occurrence to satisfy for
                """

                if new_occurrences == 0:
                    del required_characters[curr]
                else:
                    required_characters[curr] = new_occurrences

        """
        If we satisfied all characters the the required characters hashtable will be
        empty
        """
        return not required_characters


import collections
import sys


class OptimalSolution:
    def minWindow(self, searchString, t):
        """
        Interface
        ----
        :type searchString: str
        :type t: str
        :rtype: str

        Approach
        ----
        1. Make use of two pointers

        2. Ask the question:
        - Do we contract the window?
         * move the left pointer if we have satisfied by moving the right pointer
        - Do we expand the window? 
         * if we have satisfied the constraint it makes no sense to keep increasing the right pointer

        When answering these questions we have to make sure we are satisfying the constraint.

        Complexity
        ----
        t = Hashtable for target 
        s = string we are traversing (we only touch each element once with each pointer)
        Time : O(s + t)
        Space : O(s + t)
        """
        left = 0
        right = 0

        # It stores the length of maximum valid substring
        minimum = sys.maxsize
        # counts the target occurences
        counter_t = collections.Counter(t)
        counter_search = collections.defaultdict(int)
        count = 0
        minimum_window = ""

        # Here we use the 2 pointers approach
        while right < len(searchString):
            counter_search[searchString[right]] += 1
            if searchString[right] in counter_t:
                # if the number of chars is <= the occurences in the target string
                # increment the count
                # NOTE: it doesn't make sense to keep including chars if we already have enough
                if counter_search[searchString[right]] <= counter_t[searchString[right]]:
                    count += 1

            # we have found a valid substring so experiment with the left pointer
            while left <= right and count == len(t):
                # we have found a better substring
                if minimum > right - left + 1:
                    minimum = right - left + 1
                    minimum_window = searchString[left: right + 1]

                # take away a char by moving the left pointer forward
                # NOTE: we have to remove this char from counter_search
                counter_search[searchString[left]] -= 1
                # if the current char is in counter_t and we don't have an excess decrement the count
                if searchString[left] in counter_t and counter_search[searchString[left]] < counter_t[searchString[left]]:
                    count -= 1

                left += 1

            # look to find a substring that satisfies the constraints
            right += 1

        return minimum_window


corpus = "whoopiepiesmakemyscalegroan"
target = "roam"
bs = BruteForceSolution()
os = OptimalSolution()
print(bs.minWindow(corpus, target))
print(os.minWindow(corpus, target))
