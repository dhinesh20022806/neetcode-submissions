class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        res = 0


        def backtrack(total, index):

            if index >= len(nums):
                if total == target:
                    res += 1
                return
            

            backtrack(total + (nums[index] * -1), index + 1)
            backtrack(total + nums[index], index + 1)
        
        backtrack(0, 0)
        return res