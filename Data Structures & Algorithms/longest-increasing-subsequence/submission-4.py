class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dfs(i, prev):

            if i == len(nums):
                return 0
            
            res = 0

            if prev < nums[i]:
                res = 1 + dfs(i + 1, nums[i])
            
            return max(res, dfs(i + 1, prev))

        return dfs(0, float("-inf"))