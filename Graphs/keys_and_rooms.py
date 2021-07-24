"""
Keys and Rooms
We are given a 2D array arr where each element (item arr(i)) represents a room. Each "room" contains a set of "keys" that unlock other rooms in arr.

You cannot open a room unless you have a key to it. By default, room 0 will be unlocked for you to enter at first.

Given arr, determine if all rooms can be opened. Return true if it is possible, false otherwise.

Example 1:
Input: [[1], [2], [3], []]
Output: true
Explanation: Room 0 has the key to room 1. Room 1 has the key to room 2. Room 2 has the key to room 3. All rooms have been opened.

Example 2:
Input: [[], [2], [3], []]
Output: false
Explanation: Room 0 has no keys and all other rooms are locked.

Constraints:
0 <= arr[i][j] <= len(arr) - 1 (all indexes will be valid)
"""


class Solution:
    def canVisitAllRooms(self, rooms):
        """
        Approach
        ----
        Use DFS to check if we can visit every room

        Complexity
        ----
        Time : O(E + V)
        Space : O(V)
        """
        vis_rooms = [False] * len(rooms)
        s = [0]
        # we start in the first room
        while len(s) != 0:
            room = s.pop()
            if not vis_rooms[room]:
                vis_rooms[room] = True
                keys = rooms[room]
                for key in keys:
                    if not vis_rooms[key]:
                        s.append(key)

        return all(vis_rooms)
