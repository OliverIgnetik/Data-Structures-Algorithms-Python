"""
IP Address Restoration
Given a "raw" ip address string s, return all "restored" ip address strings that can be recovered from s.

A "raw" ip address string is a string of digits that can have . marks inserted to create a valid ip address.

Example 1:
Input: "255255232132"
Output: ["255.255.232.132"]
Example: There is only 1 way to restore this raw ip string

Example 2:
Input: "125523213"
Output:
[
  "1.255.23.213",
  "1.255.232.13",
  "12.55.23.213",
  "12.55.232.13",
  "125.5.23.213",
  "125.5.232.13",
  "125.52.3.213",
  "125.52.32.13"
]

Constraints:
The raw ip string will only have digits 1 to 9
4 <= n <= 12
"""


class Solution:
    def restoreIpAddresses(self, rawIpString):
        """
        Interface
        ----
        :type rawIpString: str
        :rtype: list of str

        Approach
        ----
        1. Choice : (DECISION SPACE AND LOGIC)
        - choosing four segments (1-3 snippets long) -> four recursive frames 

        2. Constraints : (FILTER OUR CHOICE)
        - 0-255 -> the number has to be between 0 and 255
        - we can't have leading zeros (ie. 012.011.011.111)
        NOTE: we can't have an address like 265.0.265.196

        3. Goal : (HOW DO WE CATCH THE RECURSION)
        - we know it's successful once we have traversed the whole string ie. completed four segments 
        (or our index would be equal to the length of the string)

        Complexity
        ----
        Branching factor = 3 (we can make 3 decisions on the digits in each segment)
        Base case = O(1)
        Depth = 4 (we can only go 4 segments deep in the call stack)

        Time : O(3^4) -> O(1) it does not scale with input
        Space : O(1) the call stack does not scale with input or the output if we include it
        """
        restored_ips = []

        self.restore_ips(0, 0, [0] * 4, rawIpString, restored_ips)

        return restored_ips

    def restore_ips(
        self,
        progress_index,
        current_segment,
        ip_address_segments,
        raw_ip_string,
        restored_ips
    ):

        # If we have filled 4 segments (0, 1, 2, 3)
        # we will only record an answer if the string was decomposed fully
        if (current_segment == 4 and progress_index == len(raw_ip_string)):
            restored_ips.append(
                self.build_ip_string_from_segments(ip_address_segments))
        # in this case the string was not fully decomposed ie. we have 4 segments that are not valid
        # given the length of the raw ip string
        elif current_segment == 4:
            return

        # Generate segments to try, a segment can be 1 to 3 digits long.
        # NOTE: DECISIONS
        for seg_length in range(1, 4):
            # NOTE: CONSTRAINT
            if progress_index + seg_length > len(raw_ip_string):
                break

            # Calculate 1 index past where the segment ends in the original raw ip string
            one_past_segment_end = progress_index + seg_length

            # Extract int value from our snapshot from the raw ip string
            segment = raw_ip_string[progress_index:one_past_segment_end]
            segment_value = int(segment)

            # Check the "snapshot's" validity - if invalid break iteration
            # NOTE: CONSTRAINT, you can't have leading zeros
            if (segment_value > 255 or (seg_length >= 2 and segment[0] == '0')):
                break

            # Add the extracted segment to the working segments
            ip_address_segments[current_segment] = segment_value

            # Recurse on the segment choice - when finished & we come back here, the next loop iteration will try another segment
            self.restore_ips(progress_index + seg_length, current_segment +
                             1, ip_address_segments, raw_ip_string, restored_ips)

    # Helper Function for building IP address from Integer
    def build_ip_string_from_segments(self, segments):
        return "{}.{}.{}.{}".format(
            segments[0],
            segments[1],
            segments[2],
            segments[3]
        )


Input = "125523213"
s = Solution()
print(s.restoreIpAddresses(Input))
