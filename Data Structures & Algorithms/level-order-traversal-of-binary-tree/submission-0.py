# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        queue = deque([root])
        res = []

        while queue:

            level_res = []

            for i in range(len(queue)):
                node = queue.popleft()

                if node is None:
                    return []

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                level_res.append(node.val)
    
            res.append(level_res)
        
        return res

            




        

