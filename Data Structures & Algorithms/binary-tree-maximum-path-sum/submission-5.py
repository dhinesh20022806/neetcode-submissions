# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maxValue = -inf

        def dfs(root):
            nonlocal maxValue

            if root is None:
                return -inf

            left = dfs(root.left) 
            right =  dfs(root.right) 
            
            maxValue = max(maxValue, left + right + root.val, left, right, root.val, left + root.val, right + root.val)

            return max(root.val, left + root.val, right + root.val)
        
        dfs(root)
        return maxValue       