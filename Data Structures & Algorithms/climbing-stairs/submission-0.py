class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n
        stepOne, stepTwo = 1, 2

        for i in range(2, n):
            stepOne = stepTwo + stepOne
            stepOne, stepTwo = stepTwo, stepOne

        return stepTwo
