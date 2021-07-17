def timeDifference(times):
    '''
    :type times: list of str
    :rtype: int

    Complexity 
    Time : O(1) limited subset of minutes
    Space : O(1) limited subset of minutes
    '''
    if len(times) < 2:
        raise (ValueError('We require more then one time'))

    def timeToInt(time):
        hours = time[0:2]
        mins = time[3:5]
        res = int(hours) * 60 + int(mins)
        return res

    # total number of minutes
    seen = [False] * 24 * 60
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
            # if we have seen a time
            if prev != -1:
                minDiff = min(minDiff, i - prev)  # i - prev is the new minDiff
            # if we haven't seen any times just yet
            else:
                first = i
            # we need to update prev no matter what
            prev = i

    # manual check for the first and last time seen
    minDiff = min(minDiff, first + 24 * 60 - prev)
    return minDiff


print(timeDifference(["00:03", "23:59", "12:03"]))
