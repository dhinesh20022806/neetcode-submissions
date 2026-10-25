class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        max_count = 0


        for i in range(len(nums) -1, -1, -1):

            count = 1
            current_max = nums[i]

            for j in range(i, -1, -1):

                if current_max > nums[j]:
                    count += 1
                    current_max = nums[j]
            max_count = max(max_count, count)
        
        return max_count



