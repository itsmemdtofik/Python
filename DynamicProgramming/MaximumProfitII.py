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
     * !Approach: Top-Down(Recursive + memoization) ==> Recursive + storage
     *
     * | Metric               | Complexity                                       |
       | -------------------- | ------------------------------------------------ |
       |   Time Complexity    | `O(n * W)`                                       |
       |   Space Complexity   | `O(n * W)` for DP table + `O(n)` recursion stack |
     *
     * </pre>
"""


class MaximumProfitII:
    dp = []  # Equivalent to: public static int dp[][];

    @staticmethod
    def knapsack(weights: list[int], values: list[int], W: int, n: int) -> int:

        # Step1: Initialize the dp table with -1 (uncomputed)
        dp = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

        if n == 0 or W == 0:
            return 0

        if dp[n][W] != -1:
            return dp[n][W]

        if weights[n - 1] <= W:
            dp[n][W] = max(
                values[n - 1] + MaximumProfitII.knapsack(weights, values, W - weights[n - 1], n - 1),
                MaximumProfitII.knapsack(weights, values, W, n - 1)
            )
            return dp[n][W]

        dp[n][W] = MaximumProfitII.knapsack(weights, values, W, n - 1)
        return dp[n][W]


if __name__ == '__main__':
    weight = [1, 3, 4, 5]
    value = [1, 4, 5, 7]
    W = 7
    n = len(weight)

    max_profit = MaximumProfitII.knapsack(weight, value, W, n)
    print("Maximum Profit =", max_profit)
