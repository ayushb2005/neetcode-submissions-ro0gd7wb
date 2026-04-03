# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # if(root is None):
        #     return True
        # if(root.left and root.left.val>=root.val):
        #     return False
        # if(root.right and root.right.val <= root.val):
        #     return False
        # return self.isValidBST(root.left) and self.isValidBST(root.right)
        def dfs(node, low, high):
            if(node is None):
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        return dfs(root, -100000000000, 100000000000)
