class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp =[0] * (capacity + 1)

        for c in range(capacity + 1):
            for i in range(len(profit)):
                if weight[i] <= c:
                    dp[c] = max(dp[c],dp[c - weight[i]] + profit[i])
        return dp[capacity]

    