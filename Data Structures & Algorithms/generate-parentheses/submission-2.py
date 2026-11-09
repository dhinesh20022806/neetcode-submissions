class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        def isValid(s):
            s_open = 0

            for c in s:
                if c == "(":
                    s_open += 1
                else:
                    s_open -= 1
                if s_open < 0:
                    return False
            
            return s_open == 0
        

        listSet = set()

        def dfs(s):
            if len(s) == 2 * n:
                if isValid(s):
                    listSet.add(s)
                return
            
            if len(s) > 2 * n:
                return
            
            dfs(s + "(")
            dfs(s + ")")
        
        dfs("")
        return list(listSet)