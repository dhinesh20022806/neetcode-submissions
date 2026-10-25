class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dfs(s, wordIndex):
            if s == "":
                return True
            if s != "" and wordIndex >= len(wordDict):
                return False

            index = 0

            if len(s) < len(wordDict[wordIndex]):
                return dfs(s, wordIndex + 1)

            for i in range(len(wordDict[wordIndex])):
                index = i
                if s[i] != wordDict[wordIndex][i]:
                    return dfs(s, wordIndex + 1)
            
            if not dfs(s[index + 1:], 0):
                return dfs(s, wordIndex + 1)
            return True

        return dfs(s, 0)    
