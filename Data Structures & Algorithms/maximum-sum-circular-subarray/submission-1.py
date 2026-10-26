class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        if not nums:
            return 0

        total = gobalMax = currentMax = gobalMin = currentMin = nums[0]

        for i in range(1, len(nums)):

            currentMax = max(currentMax + nums[i], nums[i])
            gobalMax = max(gobalMax, currentMax)

            currentMin = min(currentMin + nums[i], nums[i])
            gobalMin = min(currentMin, gobalMin)
            

        if gobalMax < 0:
            return gobalMax
        
        return max(gobalMax,gobalMax - gobalMin)