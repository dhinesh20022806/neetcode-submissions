class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 



        for j in range(1, amount + 1):
            for i in range(len(coins)):
                if coins[i] <= j:
                    dp[j] = min(1 + dp[j - coins[i]], dp[j])
        
        return dp[amount]
