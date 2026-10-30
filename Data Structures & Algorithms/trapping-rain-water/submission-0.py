class Solution:
    def trap(self, height: List[int]) -> int:
        

        if not height:
            return 0

        leftMostIndex = 0
        rightMostIndex = 1
        res = 0

        while True:

            if leftMostIndex >= len(height) or rightMostIndex >= len(height):
                break
            
            leftMostValue = height[leftMostIndex]
            rightMostValue = height[rightMostIndex]

            while rightMostIndex < len(height) and leftMostValue > height[rightMostIndex]:
                rightMostIndex += 1
               
            if rightMostIndex >= len(height):
                break
            rightMostValue = height[rightMostIndex]
            
            if leftMostValue > rightMostValue:
                break

            for i in range(leftMostIndex, rightMostIndex):
                
                res += abs(height[i] - leftMostValue)
            
            leftMostIndex = rightMostIndex
            rightMostIndex += 1
        

        return res