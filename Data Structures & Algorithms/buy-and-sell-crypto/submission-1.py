class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = 0

        profit = 0

        while right < len(prices):

            print(prices[right], prices[left])

            profit=max(prices[right] - prices[left], profit)

            if right < len(prices) -1 and prices[left] > prices[right + 1]:
                right += 1
                left = right
                continue 
            
            
            right +=1
            

        return profit