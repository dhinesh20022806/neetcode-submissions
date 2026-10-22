class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if not nums:
            return True
        
        canPass = nums[0]

        for i in range(len(nums)):

            if canPass > 0:
                canPass -= 1
                if nums[i] > canPass:
                    canPass = nums[i] - 1
                continue
            
            if nums[i] == 1:
                continue
            
            if nums[i] <= 0 and i + 1 != len(nums):
                return False
            
            canPass = nums[i] - 1
        return True