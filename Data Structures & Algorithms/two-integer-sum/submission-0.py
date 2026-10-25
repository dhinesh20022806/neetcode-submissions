class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums.sort()

        left = 0
        right = len(nums) - 1

        while left < right :

            if nums[left] + nums[right] == target:
                return [left,right]
            
            if nums[left] + nums[right] > target:
                right -= 1
                continue

            if nums[left] + nums[right] < target:
                left += 1
                continue
        return []
            