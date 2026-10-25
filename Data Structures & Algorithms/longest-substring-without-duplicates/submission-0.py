class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 1

        hashSet = {s[left],}
        maxLength  = 1

        while right < len(s):

            if s[right] in hashSet or s[left] == s[right]:

                left = right
                right = right + 1
                hashSet = set()
                continue
            
            maxLength = max(maxLength, (right - left) + 1)
            hashSet.add(s[right])

            right = right + 1
            

        return maxLength