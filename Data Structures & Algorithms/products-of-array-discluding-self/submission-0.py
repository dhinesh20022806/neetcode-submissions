class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zeros = 0

        for num in nums:
            if num == 0:
                zeros += 1
            
        if zeros > 1:
            return [0 for _ in range(len(nums))]
        
        precompute = nums[0]

        for i in range(1, len(nums)):
            precompute *= nums[i]
        
        res = []

        for num in nums:

            if zeros == 0:
               res.append(precompute // num)
            
            if zeros == 1:

                if num != 0:
                    res.append(0)
                else:
                    prezero = 1
                    for i in range(len(nums)):
                        if nums[i] != num:
                            prezero *= nums[i]
                    res.append(prezero)
        return res

