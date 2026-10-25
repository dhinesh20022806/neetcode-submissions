class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]

        currentMax = currentMin = 1


        for i in range(len(nums)):

            currentMax = max(nums[i] * currentMax, nums[i] * currentMin, res)
            currentMin = min(nums[i] * currentMin, nums[i] * currentMax, res)
            res = max(currentMax, res)
        
        return res