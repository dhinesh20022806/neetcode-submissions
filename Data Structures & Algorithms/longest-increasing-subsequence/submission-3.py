class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [0 for _ in range(len(nums))]

        dp[0] = 1

        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                dp[i] = dp[i - 1]
            else:
                dp[i] = 1 + dp[i - 1]
        return dp[-1]