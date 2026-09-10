# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        max_counter = 0


        def dfs(root, currentParent):
            nonlocal max_counter

            if root is None:
                return 
            
            if root.val >= currentParent:
                print(root.val)
                max_counter += 1
            
            dfs(root.left, max(root.val, currentParent))
            dfs(root.right, max(root.val, currentParent))

        dfs(root, root.val)


        return max_counter