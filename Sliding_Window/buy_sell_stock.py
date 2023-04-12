# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

# Test Case
prices = [7,1,5,3,6,4]
output = 5 #buy on day 1, sell on day 4 (6-1)


def stock(prices):
    # Initialize
    l, r = 0, 1 # left = buy, right = sell
    profit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit_temp = prices[r] - prices[l]
            profit = max(profit, profit_temp)

        else: 
            l = r
        r += 1
    return profit

stock(prices)


# Switching l to r happens when r < l and works because it will create a greater profit for all future numbers (because r was less than l)
# Using the profit_temp and max allows for preservation of maximum profit. Ok to switch l to r even though it might not yield a greater profit
# Will never "miss out" because of forward progression of time

