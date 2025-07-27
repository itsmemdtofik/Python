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
     * !Approach: Bottom-Up(Tabulation) : Only Iterative no recursive call + storage (matrix table)
     * Step1: Create a matrix dp[][]
     * Step2: Initialize it to first rows and first column as zero
     * Step3: Main Logic
     * Step4: Return last rows and column matrix
     *
     * | Metric               | Complexity                                       |
    | -------------------- | ------------------------------------------------ |
    | **Time Complexity**  | `O(n * W)`                                       |
    | **Space Complexity** | `O(n * W)` for DP table + `O(n)` recursion stack |
     *
     * </pre>
"""


class MaximumProfitIII:
    dp = []

    @staticmethod
    def knapsack(weights: list[int], values: list[int], W: int, n: int) -> int:

        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
        # Initialization
        # Explicitly setting dp[i][j] = 0 for base cases is unnecessary in Python,
        # but included here for clarity (like Java version)

        for i in range(n + 1):
            for j in range(W + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0  # Redundant in python, But it clears for understanding

        for i in range(1, n + 1):
            for j in range(1, W + 1):
                if weights[i - 1] <= j:
                    dp[i][j] = max(
                        values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j]
                    )
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][W]


weight = [1, 3, 4, 5]
value = [1, 4, 5, 7]
W = 7
n = len(weight)

max_profit = MaximumProfitIII.knapsack(weight, value, W, n)
print("Maximum Profit =", max_profit)
