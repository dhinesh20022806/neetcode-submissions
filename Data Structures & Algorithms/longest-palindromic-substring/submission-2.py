class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        resIdx = resLen = 0

        n = len(s)
        for i in range(n - 1, -1, -1):
            for j in range(i , n):
                if s[i] == s[j] and j - i <= 2:
                    if resLen <= j - i + 1:
                        resIdx = i
                        resLen = j - i + 1
        
        return s[resIdx: resIdx + resLen]