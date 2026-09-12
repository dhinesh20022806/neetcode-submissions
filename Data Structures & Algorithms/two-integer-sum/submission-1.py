class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashset = {}

        for i in range(0, len(nums)):

            if target - nums[i] in hashset:
                return sorted([i, hashset[target - nums[i]]])    
            else:
                hashset[nums[i]] = i
            
        return []