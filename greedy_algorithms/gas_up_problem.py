"""
The Gas-Up Problem
----
The proposed situation consists of n gas stations arranged in
a conceptual ring (station i goes to station i+1 with wrap around at sequence end). 
You are given the gas contained at each station in gas where gas[i] is the gas one redeems for visiting station i.

Also given is cost where cost[i] represents the gas it takes to get from station i to station i+1. 
NOTE: The last index wraps around the array and represents the cost to go from station length - 1 to station 0.

Given gas and cost, return the index of station s where one can start and circumnavigate all stations to return to station s.
NOTE: If the tank is depleted at any point (tank < 0) then the car will stop and the start point proposed is infeasible.

If no station can yield a complete circumnavigation return -1.

Example 1:
Input:
gas: [1, 4, 3, 2, 5]
cost: [3, 1, 5, 4, 2]

Output: 4
Explanation:
If we start at station 4 the journey looks like so:

TGAA = Total Gas At Arrival
GF = Gas Filled
CTNS = Cost To Next Station

| TGAA | GF | CTNS |
|   0  |  5 |  2   |
|   3  |  1 |  3   |
|   1  |  4 |  1   |
|   4  |  3 |  5   |
|   2  |  2 |  4   |

and then the circumnavigation is complete.

Example 2:
Input:
gas: [1, 1, 1]
cost: [2, 2, 2]

Output: -1
Explanation: We can circumnavigate the stations starting at no station.

Constraints:
All entries in gas and cost will be >= 0
NOTE: If you can circumnavigate from multiple stations, return the station with lowest index
"""


class Solution:
    def findStartStation(self, gas, cost):
        """
        Interface
        ----
        :type gas: list of int
        :type cost: list of int
        :rtype: int

        Approach
        ----
        1. We loop over every station and keep track of our current tank and greedily
        assume we can start at the first station and complete the journey. 
        2. If crossing to the next station drops our gas below 0, then we reset our tank and 
        greedily assume we can start at the next station.

        Complexity 
        ----
        Time : O(N)
        Space : O(1)
        """
        # First, we check for the existence of a solution
        if sum(gas) < sum(cost):
            return -1  # No solution can exist.

        # A solution surely exists.
        station = 0

        # It will store the amount of gas left at any instant
        tank = 0

        for curr_station in range(0, len(gas)):
            tank += gas[curr_station] - cost[curr_station]
            # NOTE: cost[curr_station] is the cost of travelling from the current station to the next station

            # If amount of gas left is negative
            # We have to start from next station
            if tank < 0:
                tank = 0
                # Greedily update our station.
                station = curr_station + 1

        return station


gas = [1, 4, 3, 2, 5]
s = Solution()
cost = s.findStartStation(gas)
print(cost)
