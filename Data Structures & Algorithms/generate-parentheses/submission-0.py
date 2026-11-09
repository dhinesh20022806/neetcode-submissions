class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        listSet = set()

        def dfs(s):
            if len(s) == n * 2:
                listSet.add(s)
                return
            if len(s) > n * 2:
                return

            dfs(s + "()")
            dfs( "(" + s + ")")
            dfs("()" + s)
        
        dfs("")
        return list(listSet)