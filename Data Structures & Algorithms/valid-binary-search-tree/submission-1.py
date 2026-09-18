# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(root, upperBound, lowerBound):

            if root is None:
                return True
            
            if not dfs(root.left, root.val, lowerBound):
                return False

            if root.val >= upperBound or root.val <= lowerBound:
                return False
            

            return dfs(root.right, upperBound, root.val)
        

        return dfs(root, +inf, -inf)