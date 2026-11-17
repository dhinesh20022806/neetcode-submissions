class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        res = float("-inf")


        def dfs(i, sums):
            nonlocal res
            if i >= len(nums):
                res = max(sums, res)
                return
            
            dfs(i + 1, sums + nums[i])
            dfs(i + 1, nums[i])
        dfs(0, 0)
        return res