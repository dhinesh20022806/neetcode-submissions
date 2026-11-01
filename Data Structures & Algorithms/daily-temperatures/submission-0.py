class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        results = [0] * len(temperatures)


        for i in range(len(temperatures)):
            res = 1
            for j in range(i + 1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    results[i] = res
                    break
                res += 1
        
        return results