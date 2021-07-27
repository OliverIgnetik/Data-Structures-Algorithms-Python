"""
Compute The Median of Online Data
We get an introduction to online algorithms and how to design abstractions that support a desired api efficiently.


In this problem, you are provided with an input each time you output an answer.  You are expected to provide a new answer after each input. 
If the answer is incorrect at any time, the, the sequence terminates.  The algorithms only progresses if the answer/output is correct.


Note: output to 1 decimal point 
e.g. 17 = 17.0

Example 1:
Input: 14
Output: 14.0
Explanation: elements seen so far: [14]
median = 14

Input: 6
Output: 10.0
Explanation: elements seen so far: [14,6]
median = (14+6)/2 = 10

Input: 30
Output: 14.0
Explanation: elements seen so far: [14,6,30]
median = 14

Input: 35
Output: 22.0
Explanation: elements seen so far: [14,6,30,35]
median = (14+30)/2 = 22

Example 2:
Input: 5
Output: 5.0
Explanation: elements seen so far: [5]
median = 5

Input: 2
Output: 3.5
Explanation: elements seen so far: [5,2]
median = (5+2)/2 = 3.5

Input: 3
Output: 3.0
Explanation: elements seen so far: [5,2,3]
median = 3
"""

"""
Approach 
----
1. Use a sorted array and:
Time : O(NlogN)
- pick the middle item if we have an odd number of items
- add the middle two and divide by two and take the floor 

2. Use two heaps a two keep track of the items in the lower half and the upper half
Time : O(logN)
- median = (max_heap_lower_half.get() + min_heap_upper_half.get())//2
- NOTE: we have to ensure the heaps are different in size by at most one 
 ie. we have to make sure that they are balanced


3. Use a balanced BST so the median will be near the top
"""
from queue import PriorityQueue


class MedianManager:
    INITIAL_CAPACITY = 10

    def __init__(self):
        self.lower = PriorityQueue()
        self.upper = PriorityQueue()

    def median(self):
        # peeking is O(1)
        if self.lower.qsize() == self.upper.qsize():
            return .5 * (self.lower.queue[0] - self.upper.queue[0])
        else:
            return -self.upper.queue[0]

    def insert(self, value):
        # we put in upper if it's zero by default
        if self.upper.qsize() == 0:
            upper.put(-value)
        else:
            # if value is less then the smallest item in the upper queue put it in lower
            if (value < -self.upper.queue[0]):
                self.lower.put(value)
            # if value is bigger then the smallest item in upper but it in upper
            else:
                self.upper.put(-value)

        self.rebalance()

    def rebalance(self):
        # if upper is too big get and item from upper and put it in lower
        if self.upper.qsize() >= self.lower.qsize() + 2:
            self.lower.put(-self.upper.get())
        # if lower is too big move an item over to upper
        elif (self.lower.qsize() >= self.upper.qsize() + 1):
            self.upper.put(-self.lower.get())
