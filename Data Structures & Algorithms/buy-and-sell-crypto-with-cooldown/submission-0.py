class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        def dfs(j, isBuy):
            if j >= len(prices):
                return 0
            res = 0
            g = j
            if not isBuy:
                g += 1

            for i in range(g, len(prices)):
                if isBuy:
                    res = max(res, dfs(i + 1, False))
                else:
                    res = max(res, dfs(i + 1, True))
            
            return res - prices[j] if isBuy else prices[j] + res
        
        return max(dfs(0, True), 0)