class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = 0


        for i in range(0, len(nums)):

            current_res = nums[i] * 1
            res = max(res, current_res)

            for j in range(i + 1, len(nums)):
                current_res *= nums[j]
                res = max(res, current_res)
        
        return res