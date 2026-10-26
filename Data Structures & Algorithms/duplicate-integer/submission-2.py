class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        resSet = set()


        for n in nums:
            if n in resSet:
                return True
            resSet.add(n)
        
        return False

        