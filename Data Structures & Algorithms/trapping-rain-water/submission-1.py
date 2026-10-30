class Solution:
    def trap(self, height: List[int]) -> int:
        

        res = 0

        for i in range(len(height)):

            currentValue = leftMostValue = rightMostValue = height[i]         

            for j in range(i, len(height)):
                rightMostValue = max(rightMostValue, height[j])
            
            for j in range(i, -1, -1):
                leftMostValue = max(leftMostValue, height[j])

            res += min(leftMostValue, rightMostValue) - currentValue
        return res
