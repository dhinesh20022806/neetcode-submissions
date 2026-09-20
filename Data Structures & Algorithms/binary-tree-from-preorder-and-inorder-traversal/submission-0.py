# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        hashMap = {}

        for i in range(len(inorder)):
            hashMap[inorder[i]] = i
        
        preorder_index = 0

        def buildBinaryTree(left, right, preorder, inorder):
            nonlocal preorder_index, hashMap


            if left > right:
                return None
            

            val = preorder[preorder_index]
            node = TreeNode(val)

            inorder_index = hashMap.get(val)
            preorder_index += 1

            node.left = buildBinaryTree(left, inorder_index - 1, preorder, inorder)
            node.right = buildBinaryTree(inorder_index + 1, right, preorder, inorder)
            return node
            
        return buildBinaryTree(0, len(inorder) - 1, preorder, inorder)


        