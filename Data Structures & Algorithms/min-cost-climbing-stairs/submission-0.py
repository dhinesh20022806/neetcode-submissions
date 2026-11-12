class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        if not cost:
            return 0
        
        if len(cost) == 1:
            return cost[0]

        
        min_cost = [0] * (len(cost) + 1)


        for i in range(2, len(cost) + 1):
            min_cost[i] = min(cost[i - 1] + min_cost[i - 1], cost[i - 2] + min_cost[i - 2])
        return min_cost[-1]