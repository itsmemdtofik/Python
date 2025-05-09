# **************************
# Stock Buy and Sell – Max one Transaction Allowed
# **************************

# Given an array prices[] of length N, representing the prices of the stocks on different days, 
# the task is to find the maximum profit possible by buying and selling the stocks on different days 
# when at most one transaction is allowed. 
# Here one transaction means 1 buy + 1 Sell.

# Note: Stock must be bought before being sold.

# Examples:

# Input: prices[] = [7, 10, 1, 3, 6, 9, 2]
# Output: 8
# Explanation: Buy for price 1 and sell for price 9.

# Input: prices[] = [7, 6, 4, 3, 1]
# Output: 0
# Explanation: Since the array is sorted in decreasing order, 0 profit can be made 
# without making any transaction.

# Input: prices[] = [1, 3, 6, 9, 11]
# Output: 10
# Explanation: Since the array is sorted in increasing order, we can make 
# maximum profit by buying at price[0] and selling at price[n-1].


def stock_buy_and_sell(prices):
    """
    This function computes the maximum profit by buying and selling stocks at most once. 
    The idea is to track the minimum price encountered so far and calculate the profit if we were 
    to sell on each day.
    """
    if not prices or len(prices) < 2:
        return 0  # If there are fewer than 2 days, no transaction can occur.

    min_price = float('inf')  # Initialize minimum price as infinity.
    max_profit = 0  # Initialize maximum profit as 0.

    # Iterate through the prices to find the minimum price and maximum profit.
    for price in prices:
        if price < min_price:
            min_price = price  # Update the minimum price encountered so far.

        profit = price - min_price  # Calculate the potential profit if we sell at the current price.
        max_profit = max(max_profit, profit)  # Update the maximum profit if necessary.

    return max_profit


def another_approach(prices):
    """
    This is an alternative approach that uses the same logic as stock_buy_and_sell,
    but the min_price and max_profit are updated in a single pass using the min and max functions.
    """
    if not prices or len(prices) < 2:
        return 0  # If there are fewer than 2 days, no transaction can occur.

    min_price = float('inf')  # Initialize minimum price as infinity.
    max_profit = 0  # Initialize maximum profit as 0.

    # Iterate through the prices to find the minimum price and maximum profit.
    for price in prices:
        min_price = min(min_price, price)  # Update the minimum price.
        profit = price - min_price  # Calculate the potential profit.
        max_profit = max(max_profit, profit)  # Update the maximum profit if necessary.

    return max_profit


# Test cases
prices1 = [7, 1, 5, 3, 6, 4]  # Expected output: 5
prices2 = [7, 6, 4, 3, 1]     # Expected output: 0
prices3 = [1, 2, 1, 3, 4, 5]  # Expected output: 4
prices4 = [10, 22, 5, 75, 65, 80]  # Expected output: 75

# Using stock_buy_and_sell method
print("Max Profit for prices1:", stock_buy_and_sell(prices1))  # 5
print("Max Profit for prices2:", stock_buy_and_sell(prices2))  # 0
print("Max Profit for prices3:", stock_buy_and_sell(prices3))  # 4
print("Max Profit for prices4:", stock_buy_and_sell(prices4))  # 75

# Using another_approach method
print("Max Profit for prices1:", another_approach(prices1))  # 5
print("Max Profit for prices2:", another_approach(prices2))  # 0
print("Max Profit for prices3:", another_approach(prices3))  # 4
print("Max Profit for prices4:", another_approach(prices4))  # 75
