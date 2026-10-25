class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashSet = {}


        for c in s:

            if c in hashSet:
                hashSet[c] = hashSet[c] + 1
            else:
                hashSet[c] = 1
        

        for c in t:

            if c in hashSet:
                hashSet[c] = hashSet[c] - 1
            else:
                return False
        
        return sum(hashSet.values()) == 0
        