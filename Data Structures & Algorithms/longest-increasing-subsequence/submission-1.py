class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(i, curr):
            res = 0

            for j in range(i + 1, len(nums)):
                if nums[j] > curr[-1]:
                    curr.append(nums[j])
                    res = max(1 + dfs(j, curr), res)
                    curr.pop()

            return res

        res = 0

        for i in range(len(nums)):
            res = max(dfs(i, [nums[i]]) + 1, res)

        return res

