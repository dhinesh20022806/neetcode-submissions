class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        nums.sort()


        def twoPointer(target, index, nums):
            left = index + 1
            right = len(nums) - 1
            res = []           
            while left < right:
                if (nums[left] + nums[right]) == target:
                    res.append([nums[left], nums[right]])
                    left += 1
                    while left > 0 and nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif (nums[left] + nums[right]) > target:
                    right -= 1
                else:
                    left += 1
            return res

        finalRes = []
        for i in range(len(nums)):

            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            res = twoPointer(-nums[i], i, nums)
        
            for n in res:
                finalRes.append(n + [nums[i]])
        
        return finalRes
