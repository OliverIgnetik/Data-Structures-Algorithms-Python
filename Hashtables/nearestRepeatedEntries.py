"""
Nearest Repeated Entries In An Array
Given an array words of words return the distance between the nearest repeated entries.

If no entry is repeated return -1.

Example 1:
Input:
[
  "This",
  "is",
  "a",
  "sentence",
  "with",
  "is",
  "repeated",
  "then",
  "repeated"
]
Output: 2
Explanation: "repeated" (index 6) and "repeated" (index 8) are 2 positions away.

Example 2:
Input:
[
  "This",
  "is",
  "a"
]
Output: -1
Explanation: There are no repeated entries.
"""
import sys


class Solution:
    def distanceOfClosestRepeatedEntries(self, sentence):
        """
        Interface
        ----
        :type sentence: list of str
        :rtype: int

        Complexity
        ----
        Time : O(N)
        Space : O(N)
        """
        # Create a Hash Map for storing the Last index where word[i] occured
        word_to_index_last_seen_at = {}

        # It stores the value which is greater than max ans possible.
        # This is done to check the case of -1
        nearest_repeated_entry_distance = sys.maxsize

        # Traverse through all the words in the string
        for i in range(0, len(sentence)):

            # Extract the word at index i
            word = sentence[i]

            # Check if that word has previously occured in the Hash Map
            if word in word_to_index_last_seen_at:

                # If the word has occured earlier
                # The map value would be contianing its last occurance
                # Take the ans as minimum of ans and the difference between i and previous occurance
                last_appearance_index = word_to_index_last_seen_at[word]
                distance_to_last_appearance = i - last_appearance_index

                nearest_repeated_entry_distance = min(
                    nearest_repeated_entry_distance,
                    distance_to_last_appearance
                )

            # Update the new occurance
            word_to_index_last_seen_at[word] = i

        return -1 if nearest_repeated_entry_distance == sys.maxsize else nearest_repeated_entry_distance


i = [
    "This",
    "is",
    "a",
    "sentence",
    "with",
    "is",
    "repeated",
    "then",
    "repeated"
]

s = Solution()
print(s.distanceOfClosestRepeatedEntries(i))
