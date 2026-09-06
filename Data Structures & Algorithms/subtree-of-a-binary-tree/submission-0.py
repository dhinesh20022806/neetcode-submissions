# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        isSubRoot = False

        def subRootCheck(node1, node2):

            if node1 is None and node2 is None:
                return True
            
            if node1 is None or node2 is None:
                return False
            
            if not subRootCheck(node1.left, node2.left):
                return False
            
            if node1.val != node2.val:
                return False
            return subRootCheck(node1.right, node2.right)

        def dfs(root, subRoot):
            nonlocal isSubRoot


            if root is None:
                return 
            
            print(root, subRoot)
            print(root.val, subRoot.val)
            if root.val == subRoot.val:
                isSubRoot = subRootCheck(root, subRoot)
            
            if isSubRoot:
                return 

            dfs(root.left, subRoot)
            dfs(root.right, subRoot)
        dfs(root, subRoot)
        return isSubRoot