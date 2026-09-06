# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        lists_sorted = []

        def pre_order(root, lists_sorted):


            if root is None:
                lists_sorted.append("#")
                return
            
            lists_sorted.append(str(root.val))
            pre_order(root.left, lists_sorted)
            pre_order(root.right, lists_sorted)
        
        pre_order(root, lists_sorted)

        return ",".join(lists_sorted)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        node_values = iter(data.split(","))

        def dfs(node_values):
            val = next(node_values)

            if val == "#":
                return None
            

            node = TreeNode(int(val))

            node.left = dfs(node_values)
            node.right = dfs(node_values)
        
            return node
        
        return dfs(node_values)
