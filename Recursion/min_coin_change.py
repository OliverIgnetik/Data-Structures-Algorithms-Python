from nose.tools import assert_equal


def rec_coin(target, coins):
    '''
    INPUT: Target change amount and list of coin values
    OUTPUT: Minimum coins needed to make change

    Note, this solution is not optimized.
    '''

    # Default to target value
    min_coins = target

    # Check to see if we have a single coin match (BASE CASE)
    if target in coins:
        return 1

    else:

        # for every coin value that is <= than target
        for i in [c for c in coins if c <= target]:

            # Recursive Call (add a count coin and subtract from the target)
            num_coins = 1 + rec_coin(target-i, coins)

            # Reset Minimum if we have a new minimum
            if num_coins < min_coins:

                min_coins = num_coins

    return min_coins


# consider using decorators to encapsulate memoization

def rec_coin_dynam(target, coins, known_results):
    '''
    INPUT: This function takes in a target amount and a list of possible coins to use.
    It also takes a third parameter, known_results, indicating previously calculated results.
    The known_results parameter shoud be started with [0] * (target+1)

    OUTPUT: Minimum number of coins needed to make the target.
    '''

    # Default output to target
    min_coins = target

    # Base Case
    if target in coins:
        known_results[target] = 1
        return 1

    # Return a known result if it happens to be greater than 0
    elif known_results[target] > 0:
        return known_results[target]

    else:
        # for every coin value that is <= than target
        for i in [c for c in coins if c <= target]:

            # Recursive call, note how we include the known results!
            num_coins = 1 + rec_coin_dynam(target-i, coins, known_results)

            # Reset Minimum if we have a new minimum
            if num_coins < min_coins:
                min_coins = num_coins

                # Reset the known result
                known_results[target] = min_coins

    return min_coins


def bottom_up_solution(n, coins):

    # intialize the array
    arr = [0] + [n]*(n)

    for i in range(1, len(arr)):
        min_coins = n
        for coin in [c for c in coins if c <= i]:
            min_coins = min(arr[i-coin] + 1, min_coins)

        arr[i] = min_coins

    return arr[n]


class TestCoins(object):

    def check(self, solution):
        coins = [1, 5, 10, 25]
        assert_equal(solution(45, coins, [0]*(45+1)), 3)
        assert_equal(solution(23, coins, [0]*(23+1)), 5)
        assert_equal(solution(74, coins, [0]*(74+1)), 8)

        print('Passed all tests.')


# Run Test
# test = TestCoins()
# test.check(rec_coin_dynam)

# print(bottom_up_solution(6, [1, 2, 5]))


# dynamic solution
target = 23
coins = [1, 2, 5, 10, 20]
known_results = [0]*(target+1)

print(rec_coin_dynam(target, coins, known_results))
