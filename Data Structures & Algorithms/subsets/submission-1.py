class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        res = [[]]

        if len(nums) >= 2:
            for i in range(len(nums)):
                res.append([nums[i]])
                for j in range(i + 1, len(nums)):
                    res.append([nums[i], nums[j]])
        
        res.append(nums)
        
        return res