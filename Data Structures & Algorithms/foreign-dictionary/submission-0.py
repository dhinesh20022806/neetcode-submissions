class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        grahp = {c: set() for w in words for c in w }

        for i in range(0, len(words) - 1):

            w1, w2 = words[i], words[i + 1]

            wordonelen = len(w1)
            wordtwolen = len(w2)

            minlen = min(wordonelen, wordtwolen)

            if wordtwolen < wordonelen and w1[:minlen] == w2[:minlen]:
                return ""
            
            for j in range(len(w1)):
                if j >= len(w2):
                    break
                if w1[j] != w2[j]:
                    grahp[w1[j]].add(w2[j])
                    break
            
        visited = {}
        res = []
        def dfs(c):
            if c in visited:
                return visited[c]
            
            visited[c] = True

            for adj in grahp[c]:
                if dfs(adj):
                    return True
            
            visited[c] = False

            res.append(c)
        

        for char in grahp:
            if dfs(char):
                return ""
        res.reverse()

        return "".join(res)