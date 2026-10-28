class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        leftpointer = 0
        rightpointer = len(numbers) -1


        while leftpointer < rightpointer:

            sumoftwo = numbers[leftpointer] + numbers[rightpointer]

            if sumoftwo == target:
                return [numbers[leftpointer], numbers[rightpointer]]
            
            if sumoftwo > target:
                rightpointer -= 1
            else:
                leftpointer += 1
            
        return []