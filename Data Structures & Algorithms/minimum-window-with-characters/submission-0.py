class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        tCounts = defaultdict(int)

        for c in t:
            tCounts[c] += 1

        window = {}

        have = 0
        need = len(tCounts)

        resList, res = [-1, -1], float("inf")

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in tCounts:
                have += 1

            while left < len(s) and have == need:

                if (right - left) + 1 < res:
                    resList = [left, right]



        
    



