def solution(unsorted_prices, max_price):

    # list of 0s at indices 0 to max_price
    prices_to_counts = [0] * (max_price+1)

    # populate prices
    for price in unsorted_prices:
        prices_to_counts[price] += 1

    # populate final sorted prices
    sorted_prices = []
    # For each price in prices_to_counts
    for price, count in enumerate(prices_to_counts):
        # for the number of times the element occurs
        for _ in range(count):
            # add it to the sorted price list
            sorted_prices.append(price)

    return sorted_prices


print(solution([2, 2, 2, 7, 3, 2, 9], 10))
