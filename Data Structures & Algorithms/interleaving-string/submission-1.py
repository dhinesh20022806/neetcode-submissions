class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if not (len(s1) + len(s2)) == len(s3):
            return False

        if s1 == s2 == s3:
            return True 

        def dfs(i, j, k):
            
            if k == len(s3):
                return True
            

            if i < len(s1) and j < len(s2) and s1[i] == s2[j] == s3[k]:
                if dfs(i + 1, j, k + 1) or dfs(i , j+ 1, k + 1):
                    return True
                return False
            
            if i < len(s1) and  s1[i] == s3[k]:
                if not dfs(i + 1, j, k + 1):
                    return False
                return True
            
            if j < len(s2) and s2[j] == s3[k]:
                if not dfs(i , j+ 1, k+1):
                    return False
                return True
            
            return False
        
        return dfs(0, 0, 0)