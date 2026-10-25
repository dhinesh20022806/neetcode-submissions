class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = float('-inf')


        negativeNumber = 0

        for i in range(0, len(nums)):

            if nums[i] < 0:
                negativeNumber += 1
        

        if negativeNumber % 2 == 0:

            res = nums[0] * 1
            for i in range(1, len(nums)):

                currentNum = nums[i] * 1

                res *= currentNum
        else:
            currentMax = float('-inf')
            for i in range(0, len(nums)):

                if currentMax == float('-inf'):
                    currentMax = nums[i]
                    continue

                if nums[i] < 0:
                    res = max(currentMax, res)
                    currentMax = float('-inf')
                    continue
                
                currentMax *= nums[i] * 1
                print("currentMax ", currentMax)
            
            res = max(currentMax, res)
        
        return res


        
