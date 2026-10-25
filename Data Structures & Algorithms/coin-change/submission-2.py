class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        def dfs(balance, i):
            if balance == 0:
                return 0

            if i >= len(coins) or balance < 0:
                return float("inf")

            take = 1 + dfs(balance - coins[i], i)
            skip = dfs(balance, i + 1)

            return min(take, skip)
        
        res =  dfs(amount, 0)

        return -1 if res == float("inf") else res