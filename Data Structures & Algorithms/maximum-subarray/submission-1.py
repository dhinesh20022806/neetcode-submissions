class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        res = currentMax = nums[0]

        for i in range(1, len(nums)):
            currentMax = max(nums[i] + currentMax, nums[i])
            res = max(currentMax, res)
        return res
    

