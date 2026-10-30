class Solution:
    def trap(self, height: List[int]) -> int:
        

        leftMostValues = []
        rightMostValues = []

        leftMostValue = 0

        for val in height:
            leftMostValue = max(leftMostValue, val)
            leftMostValues.append(leftMostValue)

        rightMostValue = 0

        for j in range(len(height) -1, -1, -1):
            rightMostValue = max(rightMostValue, height[j])
            rightMostValues.append(rightMostValue)
        

        res = 0
        rightMostValues.reverse()
    


        for i in range(len(height)):
            res += min(leftMostValues[i], rightMostValues[i]) - height[i]
        
        return res