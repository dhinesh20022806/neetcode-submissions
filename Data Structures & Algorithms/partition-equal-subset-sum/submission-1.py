class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        
        def backtrack(i, partone, parttwo):
            if len(partone) > 0 and len(parttwo) > 0 and sum(partone) == sum(parttwo):
                return True
            
            if i == len(nums):
                return False
            
            partone.append(nums[i])
            if backtrack(i + 1, partone, parttwo):
                return True
            partone.pop()
            parttwo.append(nums[i])

            return backtrack(i  + 1, partone, parttwo)
        
        return backtrack(0, [], [])