class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        
        def dfs(i, arr):

            if i == len(arr):
                return 0
            
            res = dfs(i + 1, arr)

            curr = arr[0:i] + arr[i + 1:]

            first = 1
            second = 1

            if i - 1 >= 0:
                first = arr[i - 1]
            if i + 1 < len(arr):
                second = arr[i + 1]

            return max(res, dfs(0, curr) + (first * arr[i] * second)) 

        return dfs(0, nums)



