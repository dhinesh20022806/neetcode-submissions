class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()
        self.backtrack([], nums, [False] * len(nums))
        return self.res
    
    def backtrack(self, perm, nums, pick):

        if len(perm) == len(nums):
            self.res.append(perm[:])
            return
        
        for i in range(len(nums)):
            if not pick[i]:
                if i + 1 < len(nums) and  nums[i] == nums[i + 1] and not pick[i + 1]:
                    continue 
                pick[i] = True
                perm.append(nums[i])
                self.backtrack(perm, nums, pick)
                pick[i] = False
                perm.pop()
        return 