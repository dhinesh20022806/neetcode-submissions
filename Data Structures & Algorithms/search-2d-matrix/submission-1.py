class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        left = 0
        right = len(matrix)


        while left <= right:

            mid = (left + right) // 2

            if mid < len(matrix) and matrix[mid][0] <= target and matrix[mid][len(matrix[0])-1] >= target:

                # ro find

                l = 0
                r = len(matrix[0])

                while l <= r:

                    m = (l + r) // 2

                    if matrix[mid][m] == target:

                        return True
                    elif matrix[mid][m] > target:
                        r = m - 1
                    else:
                        l = m + 1
                
                return False
            elif mid < len(matrix) and matrix[mid][0] > target:

                right = mid - 1
            else:
                left = mid + 1
        
        return False
        