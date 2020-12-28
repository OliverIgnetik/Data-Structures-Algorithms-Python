#####################################################
# EXAMPLE
#####################################################
# For example, if you were given the list of stock prices:

# prices = [12,11,15,3,10]

# Then your function would return the maximum possible profit, which would be 7 (buying at 3 and selling at 10).

#####################################################
# SOLUTION
#####################################################

def profit(stock_prices):

    # Check length
    if len(stock_prices) < 2:
        raise Exception('Need at least two stock prices!')

    # Start minimum price marker at first price
    min_stock_price = stock_prices[0]

    # Start off with an initial max profit
    max_profit = stock_prices[1] - stock_prices[0]

    # Skip first index of 0
    for price in stock_prices[1:]:

        # NOTE THE REORDERING HERE DUE TO THE NEGATIVE PROFIT TRACKING

        # Check the current price against our minimum for a profit
        # comparison against the max_profit
        comparison_profit = price - min_stock_price

        # Compare against our max_profit so far
        max_profit = max(max_profit, comparison_profit)

        # Check to set the lowest stock price so far
        min_stock_price = min(min_stock_price, price)

    return max_profit


print('OUPUT')
print('-'*60)
print(profit([10, 8, 2, 0, 4, 10]))
