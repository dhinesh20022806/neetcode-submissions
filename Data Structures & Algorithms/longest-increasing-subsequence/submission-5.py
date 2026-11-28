class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = {}
        def dfs(i, prev):

            if i == len(nums):
                return 0

            if (i, prev) in memo:
                return memo[(i, prev)]
            
            res = 0

            if prev < nums[i]:
                res = 1 + dfs(i + 1, nums[i])
            
            memo[(i, prev)] = max(res, dfs(i + 1, prev))
            return memo[(i, prev)]

        return dfs(0, float("-inf"))