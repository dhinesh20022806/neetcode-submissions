class Solution:
    def canPartition(self, nums: List[int]) -> bool:
       return sum(nums) % 2 == 0