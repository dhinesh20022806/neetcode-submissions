class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        listSet = set()

        def dfs(s):
            if len(s.strip()) == n * 2:
                listSet.add(s.strip())
                return
            if len(s.strip()) > n * 2:
                return

            dfs(s + "()")
            dfs( "(" + s + ")")
            dfs("()" + s)
            if len(s.strip()) > 1:
                dfs(s + s)
        
        dfs("")
        return list(listSet)