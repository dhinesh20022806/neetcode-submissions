# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        max_height = 0


        def recursive_height(root):
            nonlocal max_height


            if root is None:
                return 0
            
            left = recursive_height(root.left)
            right = recursive_height(root.right)



            max_height = max(max_height, 1 + left, 1 + right)


            return 1 + max(left, right)
        
        recursive_height(root)
        return max_height
