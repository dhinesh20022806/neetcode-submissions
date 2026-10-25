class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        for i in range(len(nums)):

            j = i + 1

            if j == len(nums):
                break
            
            if nums[i] == nums[j]:
                return True
        return False

        