class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(j, buying):
            if j >= len(prices):
                return 0

            if (j, buying) in memo:
                return memo[(j, buying)]

            cooldown = dfs(j + 1, buying)

            if buying:
                buy = dfs(j + 1, not buying)
                memo[(j, buying)] = max(buy - prices[j], cooldown)
            else:
                sell = dfs(j + 2, not buying)
                memo[(j, buying)] =  max(sell + prices[j], cooldown)

            return memo[(j, buying)]
        return dfs(0, True)