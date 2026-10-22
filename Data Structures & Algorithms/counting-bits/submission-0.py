class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = []
        for i in range(n + 1):

            x = i

            count = 0

            while x > 0:

                count += x & 1

                x >>= 1
            
            res.append(count)
        
        return res