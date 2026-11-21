class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}
        

        def dfs(j, isBuy):
            if j >= len(prices):
                return 0
            res = 0

            if (j, isBuy) in memo:
                return memo[(j, isBuy)]

            g = j

            if not isBuy:
                g += 1
            

            for i in range(g, len(prices)):
                if isBuy:
                    res = max(res, dfs(i + 1, False))
                    if i == 1:
                        print(prices[i])
                        print(res)
                else:
                    res = max(res, dfs(i + 1, True))
            
            memo[(j, isBuy)] = res - prices[j] if isBuy else prices[j] + res

            return memo[(j, isBuy)]
        
        res = 0

        for i in range(len(prices)):
            res = max(dfs(i, True), res)
        return dfs(0, True)