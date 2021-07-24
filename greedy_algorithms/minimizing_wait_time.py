"""
Scheduling To Minimize Wait Time
Given a set of tasks tasks where index i corresponds to task i+1's duration (the first task, index 0, is task 1), return a sequence representing a schedule of the tasks that minimizes overall schedule wait time.

Example 1:
Input: [1, 1000]
Output: [1, 2]
Explanation: We do task 1. Task 2 waits 1 unit of time for task 1 to finish (task 1 takes 1 unit of time). We then do task 2. Total wait time: 1.

Example 2:
Input: [3, 1, 2]
Output: [2, 3, 1]
Explanation:
We do task 2 first. Task 3 & 1 have to wait for task 2 to finish.

Task 2 takes 1 unit of time, so task 3 & 1 each are waiting (individually) 1 unit of time adding up to 2 units waited in total for task 2.
NOTE: we have to sum

We then do task 3. Task 1 has to wait for task 3 to finish.

Task 3 takes 2 units of time, so task 1 waits 2 units of time. This is 2 more units of schedule wait time.

We finally do task 1. The cumulative schedule wait time is 4.

Constraints:
task[i] > 0
If more than 1 task has the same Duration, The task which has appeared earlier in the input should appear earlier in the output as well.
"""


class Solution:
    def minimizeWaitTime(self, tasks):
        """
        Interface
        ----
        :type tasks: list of int
        :rtype: list of int

        Approach
        ----
        1. The overall wait time is a sum that every task has to wait
        2. We need to choose the best option at each step in the algorithm
        ie. choose the task with the smallest waiting time

        Proof
        ----
        We make use of an exchange arguement to transform the optimum 
        solution to the greedy solution

        GREEDY : g1, g2, g3, ..., gn
        OPTIMAL : a1, a2, a3, ..., an 

        1.If the greedy solution is not optimal there must be some gi != ai
        2. If there is only one pair that is out of order we could just swap them
        3. But if we swap the pair then we know that the wait time will be longer


        Complexity
        ----
        Time : O(NlogN)
        Space : O(N)

        """

        # Map the task duration along with its position
        # NOTE: in the array tasks the value at index i is the wait time for task (i+1)
        task_mappings = [{'duration': duration, 'taskNumber': i + 1}
                         for i, duration in enumerate(tasks)]

        # Sort the taskTuples according to the tasksDuration in
        # ascending order
        def task_cmp(a):
            return a['duration']
        task_mappings.sort(key=task_cmp)

        # Return the array of task Positions obtained after sorting
        return [item['taskNumber'] for item in task_mappings]


times = [3, 1, 2]
# waiting times:
# task 1 = 1
# task 2 = 3
# task 3 = 1

# optimal sorting is:
# [3, 1, 2]
# NOTE: This is a greedy solution because we make the local optimum choice
s = Solution()
print(s.minimizeWaitTime(times))
