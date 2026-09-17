class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        if len(s) == 0:
            return 0

        left = 0
        right = 1

        hashSet = {s[left]}
        maxLength  = 1

        while right < len(s) and left < len(s):

            if s[right] in hashSet or s[left] == s[right]:
                hashSet.discard(s[left])
                left = left + 1
                if left == right:
                    right = right + 1
                continue
            
            maxLength = max(maxLength, (right - left) + 1)
            hashSet.add(s[right])

            right = right + 1
            

        return maxLength