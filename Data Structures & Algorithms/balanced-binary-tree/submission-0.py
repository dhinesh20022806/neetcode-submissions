# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def get_height_imbalance(root):
            if root is None:
                return 0
        

            left = get_height_imbalance(root.left)
            right = get_height_imbalance(root.right)


            if left == -1 or right == -1:
                return -1
            

            if abs(left - right)  > 1:
                return -1
            

            return 1 + max(left, right)

        return get_height_imbalance(root) != -1

        

