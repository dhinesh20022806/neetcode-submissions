class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        newList = sorted(nums)

        total = 1

        current = 1

        for i in range(1, len(newList)):

            if abs(newList[i] - newList[i - 1]) == 1:
                current += 1
            
            if abs(newList[i] - newList[i - 1]) > 1:
                total = max(total, current)
                current = 1
        
        return max(total, current)
            



        