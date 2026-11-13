class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return []
        
        if len(nums) == 1:
            return [nums]
        
        perm = self.permute(nums[1:])

        res = []

        for p in perm:
            for i in range(0, len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        
        return res
