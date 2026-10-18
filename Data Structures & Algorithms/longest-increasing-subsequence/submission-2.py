class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memo = {}

        def dfs(i, curr):
            res = 0

            if i in memo:
                return memo[i]

            for j in range(i + 1, len(nums)):
                if nums[j] > curr[-1]:
                    curr.append(nums[j])
                    res = max(1 + dfs(j, curr), res)
                    curr.pop()

            memo[i] = res

            return res

        res = 0

        for i in range(len(nums)):
            res = max(dfs(i, [nums[i]]) + 1, res)
        

        return res

