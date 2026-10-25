class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        coins.sort()
        noOfCoin = float("inf")

        for i in range(0, len(coins)):

            balance = amount
            count_coins = 0
            for j in range(i, -1, -1):

                while balance >= coins[j]:
                    balance -= coins[j]
                    count_coins += 1

            if balance == 0:
                noOfCoin = min(noOfCoin, count_coins) 
        

        
        return -1 if noOfCoin == float("inf") else noOfCoin