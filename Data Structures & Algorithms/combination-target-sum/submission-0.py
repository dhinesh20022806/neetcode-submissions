class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res = []


        copyList = []
        def dfs(copyList, i):

            currentTotal = sum(copyList)

            if currentTotal > target or i >= len(nums):
                return

            if currentTotal == target:
                res.append(copyList.copy())
                return

            copyList.append(nums[i])
            dfs(copyList, i)


            copyList.pop()


            dfs(copyList, i+1)
        
        dfs(copyList, 0)

        return res



