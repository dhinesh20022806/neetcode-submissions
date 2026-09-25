class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxWater = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            maxWater = max(maxWater, (right - left) * min(heights[left], heights[right]))

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return maxWater
        