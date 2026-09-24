class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = {}

        for key in strs:
            hashMap["".join(sorted(key))] = []
        
        for string in strs:
                hashMap["".join(sorted(string))].append(string)

        
        # print(hashMap.values())
        
        return [value for value in hashMap.values()]
        