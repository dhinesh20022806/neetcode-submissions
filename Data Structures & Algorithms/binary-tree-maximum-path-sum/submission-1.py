# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(root):

            if root is None:
                return -inf

            left = dfs(root.left) 
            right =  dfs(root.right) 
            

            return max(left + root.val, right + root.val, root.val, root.val + right + left, left, right)
        
        return dfs(root)        