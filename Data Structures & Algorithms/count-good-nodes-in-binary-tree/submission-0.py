# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import inf

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        current_max = -inf
        max_counter = 0


        def dfs(root):
            nonlocal current_max
            nonlocal max_counter

            if root is None:
                return 
            

            if root.val >= current_max:
                current_max = root.val
                max_counter += 1
            
            dfs(root.left)
            dfs(root.right)

        dfs(root)


        return max_counter