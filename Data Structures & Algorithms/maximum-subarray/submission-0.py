class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        res = currentMax = nums[0]

        for i in range(1, len(nums)):

            if currentMax < nums[i]:
                currentMax = nums[i]
            else:
                currentMax += nums[i]
            
            res = max(currentMax, res)
        return res
    

