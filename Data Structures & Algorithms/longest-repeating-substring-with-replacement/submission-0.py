class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = right = 0

        hashMap = defaultdict(int)

        length = 1

        if len(s) == 1:
            return length

        while left <= right and right < len(s):

            if (right + 1 < len(s) and s[right] != s[right + 1]) or k > 0:
                count = hashMap[s[right]]
                if count > 0:
                    k -= 1
                hashMap[s[right]] += 1
                length = max(length, (right - left ) + 1)
                right += 1
            else:
                if hashMap[s[left]] > 1:
                    k += 1
                hashMap[s[left]] -= 1
                left += 1

    
        return length