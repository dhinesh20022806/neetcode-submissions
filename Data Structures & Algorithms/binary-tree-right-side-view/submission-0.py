# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        
        right_nodes = []

        queue = deque([root])

        while queue:

            level_size = len(queue)

            for i in range(len(queue)):
                
                root = queue.popleft()

                if  i == level_size - 1:
                    right_nodes.append(root.val)
                

                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                
        
            

        
        return right_nodes