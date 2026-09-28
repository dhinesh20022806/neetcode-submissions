class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        tCounts = defaultdict(int)

        for c in t:
            tCounts[c] += 1

        window = {}

        have = 0
        need = len(tCounts)
        left = 0

        resList, res = [-1, -1], float("inf")

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in tCounts and window[c] == tCounts[c]:
                have += 1

            while have == need:
                if right - left + 1 < res:
                    res = right - left + 1
                    resList = [left, right]
                window[s[left]] -= 1
                if s[left] in tCounts and window[s[left]] < tCounts[s[left]]:
                    have -= 1
                left += 1
            
        return "" if res == float("inf") else s[resList[0]:resList[1] + 1]

        
    



