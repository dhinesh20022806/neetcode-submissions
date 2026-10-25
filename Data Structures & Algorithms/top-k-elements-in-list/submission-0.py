class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashFrequent = {}

        for num in nums:
            hashFrequent[num] = hashFrequent.get(num, 0) + 1
        
        res = []
        for _, (key, value) in enumerate(hashFrequent.items()):

            if value >= k:
                res.append(key)
        
        return res
