class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]

        currentMax = currentMin = 1


        for i in range(len(nums)):
            tmp = nums[i] * currentMax
            currentMax = max(nums[i] * currentMax, nums[i] * currentMin, nums[i])
            currentMin = min(nums[i] * currentMin, tmp, nums[i])
            res = max(currentMax, res)
        
        return res