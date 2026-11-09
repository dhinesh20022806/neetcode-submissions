class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        

        def dfs(curr, index, total):
            if index >= len(nums):
                return 0
            
            curr.append(nums[index])
            res1 = dfs(curr, index + 1, total ^ nums[index])
            curr.pop()
            res2 = dfs(curr, index + 1, total)

            return (total ^ nums[index]) + res1 + res2

        return dfs([], 0, 0)