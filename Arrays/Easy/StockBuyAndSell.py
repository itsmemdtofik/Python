"""
 * ! Stock Buy and Sell – Max one Transaction Allowed.
 * ! Time Complexity : O(n) Space Complexity: O(1)
 *
 * Given an array prices[] of length N, representing the prices of the stocks on
 * different days, the task is to find the maximum profit possible by buying and
 * selling the stocks on different days when at most one transaction is allowed.
 * Here one transaction means 1 buy + 1 Sell.
 *
 * Note: Stock must be bought before being sold.
 *
 * Examples:
 *
 * Input: prices[] = {7, 10, 1, 3, 6, 9, 2}
 * Output: 8
 * Explanation: Buy for price 1 and sell for price 9.
 *
 *
 * Input: prices[] = {7, 6, 4, 3, 1}
 * Output: 0
 * Explanation: Since the array is sorted in decreasing order, 0 profit can be
 * made without making any transaction.
 *
 * Input: prices[] = {1, 3, 6, 9, 11}
 * Output: 10
 * Explanation: Since the array is sorted in increasing order, we can make
 * maximum profit by buying at price[0] and selling at price[n-1]
 *
"""


def stockBuyAndSellUsingNestedLoop(prices):
    maxProfit = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            maxProfit = max(maxProfit, prices[j] - prices[i])
    return maxProfit


def stockBuyAndSell(prices):
    minimumSoFar = prices[0]
    maxProfit = 0

    # Update the minimum value seen so far if we see smaller
    for price in range(1, len(prices)):
        minimumSoFar = min(minimumSoFar, prices[price])

        # Update the result if we get more profit
        maxProfit = max(maxProfit, prices[price] - minimumSoFar)

    return maxProfit


def stockBuyAndSellII(prices):
    if not prices or len(prices) < 2:
        return 0

    minimumPriceSoFar = float('inf')
    maxProfit = 0

    for price in prices:
        minimumPriceSoFar = min(minimumPriceSoFar, price)  # Update min price so far
        minimumProfitSoFar = price - minimumPriceSoFar  # Profit if sold today
        maxProfit = max(maxProfit, minimumProfitSoFar)  # Update max profit
    return maxProfit


values = [7, 1, 0, 5, 3, 6, 4]
print(stockBuyAndSell(values))

if __name__ == "__main__":
    prices1 = [7, 10, 1, 3, 6, 9, 2]
    print(stockBuyAndSellUsingNestedLoop(prices1))

    prices2 = [7, 1, 5, 3, 6, 4]
    print(stockBuyAndSellII(prices2))  # Output: 5 (Buy at 1, sell at 6)
