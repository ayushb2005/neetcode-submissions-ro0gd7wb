# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        recursively swap self.left and self.right 
        '''
        # if(root):
        #     #swap nodes
        #     intermediateNode = root.left
        #     root.left = root.right
        #     root.right = intermediateNode
        #     #call it on the trees to do the same
        #     self.invertTree(root.left)
        #     self.invertTree(root.right)
        # return root
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

