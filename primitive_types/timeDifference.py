from typing import List


def timeToInt(time: str) -> int:
    hours, mins = time.split(':')
    res = int(hours) * 60 + int(mins)
    return res


def timeDifference(times: List[str]) -> int:
    '''
    :type times: list of str
    :rtype: int

    General Approach
    Trade Space for time Complexity
    * dictionaries and sets are not ordered 

    NOTE: Key takeaway is that given the limited size and the fact
    that duplicates yield a trivial answer the time and space won't scale

    Complexity
    Time : O(1) limited subset of minutes
    Space : O(1) limited subset of minutes
    '''
    if len(times) < 2:
        raise (ValueError('We require more then one time'))

    # total number of minutes
    seen = [False] * 24 * 60
    # If we encounter duplicate times this means the time difference
    # is zero. The maximum amout of different times is limited to the
    # total number of minutes in 24 hours no matter the size of the input
    for time in times:
        n = timeToInt(time)
        # duplicate time
        if seen[n]:
            return 0
        seen[n] = True

    prev = -1  # to hold onto the previous time
    minDiff = 24 * 60 + 1  # this is the maximum amount of time in the day
    first = -1  # to grab the value closest to 00:00

    for i in range(0, len(seen)):
        if seen[i]:
            # if we have retrieved the first item
            if prev != -1:
                minDiff = min(minDiff, i - prev)  # i - prev is the new minDiff
            # if we haven't seen any times just yet
            else:
                first = i
            # we need to update prev no matter what
            prev = i

    # manual check for the first and last time seen
    minDiff = min(minDiff, (first + 24 * 60) - prev)
    return minDiff


print(timeDifference(["00:00", "21:37", "00:50", "22:10", "21:40", "22:15", "11:40", "03:30", "04:40",
      "08:24", "19:18", "16:20", "15:14", "12:59", "11:01", "23:00", "07:07", "13:13", "05:04", "03:02"]))
