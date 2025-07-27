"""
     * <pre>
     * !0/1 Knapsack Problems
     * You are given N items. Each item has:
     * A weight w[i]
     * A value v[i]
     * You also have a knapsack with a maximum capacity W.
     * You need to choose a subset of items such that:
     * The total weight of selected items does not exceed W
     * The total value is maximized
     * You can either take an item or not (0/1 Knapsack — each item is included at most once)
     *
     * @param Examples:
     * Weights: [1, 3, 4, 5]
     * Values:  [1, 4, 5, 7]
     * Capacity(W): 7
     * !Approach: Recursion
     * Time Complexity: O(2^n) — since every item has two choices (pick or not pick), leading to exponential time.
     * Space Complexity: O(n) — due to recursive call stack depth.
     * </pre>
"""
from typing import List


class MaximumProfit:

    @staticmethod
    def knapsack(weights: List[int], values: List[int], W: int, n: int) -> int:

        if n == 0 or W == 0:
            return 0

        if weights[n - 1] <= W:
            return max(
                values[n - 1] + MaximumProfit.knapsack(weights, values, W - weights[n - 1], n - 1),
                MaximumProfit.knapsack(weights, values, W, n - 1)
            )
        else:
            return MaximumProfit.knapsack(weights, values, W, n - 1)


weight = [1, 3, 4, 5]
value = [1, 4, 5, 7]
W = 7
n = len(weight)

max_profit = MaximumProfit.knapsack(weight, value, W, n)
print("Maximum Profit =", max_profit)
