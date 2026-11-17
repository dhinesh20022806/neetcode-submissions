class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    
        res = float("-inf")
        def dfs(i, sums):
            nonlocal res
            res = max(sums, res)
            if i >= len(nums):
                return
            
            dfs(i + 1, sums + nums[i])
            dfs(i + 1, nums[i])
        dfs(0, float("-inf"))
        return res