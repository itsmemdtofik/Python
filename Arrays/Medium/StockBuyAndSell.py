"""
 * !Stock Buy and Sell - Multiple transaction is allowed.
 *
 * Given an array prices[] of size n denoting the cost of stock on each day, the
 * task is to find the maximum total profit if we can buy and sell the stocks
 * any number of times.
 *
 * Note: We can only sell a stock which we have bought earlier and we cannot
 * hold multiple stocks on any day.
 *
 * Input: prices[] = {100, 180, 260, 310, 40, 535, 695}
 * Output: 865
 * Explanation: Buy the stock on day 0 and sell it on day 3 => 310 – 100 = 210
 * Buy the stock on day 4 and sell it on day 6 => 695 – 40 = 655
 * Maximum Profit = 210 + 655 = 865
 *
 * Input: prices[] = {4, 2, 2, 2, 4}
 * Output: 2
 * Explanation: Buy the stock on day 3 and sell it on day 4 => 4 – 2 = 2
 * Maximum Profit = 2
 * </pre>
"""


def stockBuyAndSell(nums: list[int]) -> int:
    if nums is None:
        return 0

    maxProfit = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            maxProfit = maxProfit + nums[i] - nums[i - 1]
    return maxProfit


nums1: list[int] = [100, 180, 260, 310, 40, 535, 695]
print(f"Maximum Profit after Selling: {stockBuyAndSell(nums1)}")
