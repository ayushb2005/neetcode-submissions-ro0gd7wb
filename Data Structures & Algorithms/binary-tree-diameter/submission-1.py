# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        take height of each side of the subtree, and add each side 

        '''
        self.res = 0 
        def dfs(root):
            if root is None:
                return 0
            leftHeight = dfs( root.left)
            rightHeight = dfs(root.right)
            diameter = leftHeight + rightHeight
            self.res = max(diameter, self.res)
            return 1+max(leftHeight, rightHeight)
        dfs(root)
        return self.res