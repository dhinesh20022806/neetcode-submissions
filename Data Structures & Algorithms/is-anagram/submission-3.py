class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26
        for c in s:
            arr[ord('a') - ord(c)] += 1
        
        for c in t:
            arr[ord('a') - ord(c)] -= 1
        
        return all(n == 0 for n in arr)