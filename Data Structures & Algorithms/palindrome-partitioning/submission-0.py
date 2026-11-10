class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        def isPalindromic(s):
            left = 0
            right = len(s) - 1
            if len(s) / 2 == 0:

                while (left <= right):

                    if s[left] != s[right]:
                        return False
                    
                    left += 1
                    right -= 1
            else:

                while (left < right):
                    if s[left] != s[right]:
                        return False
                    left += 1
                    right -= 1

            return True
        res = []
        parts = []

        def backtrack(i):

            if i >= len(s):
                res.append(parts.copy())
                return
            

            for j in range(i, len(s)):

                if isPalindromic(s[i:j + 1]):
                    parts.append(s[i:j+1])
                    backtrack(j + 1)
                    parts.pop()
        
        backtrack(0)
        
        return res




