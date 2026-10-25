class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dfs(s, wordIndex):

            print(s, wordIndex, wordDict)

            if s == "":
                return True
            if s != "" and wordIndex >= len(wordDict):
                return False

            index = 0

            for i in range(len(wordDict[wordIndex])):
                index = i
                if s[i] != wordDict[wordIndex][i]:
                    return dfs(s, wordIndex + 1)
            
            return dfs(s[index + 1:], 0)

        return dfs(s, 0)    
