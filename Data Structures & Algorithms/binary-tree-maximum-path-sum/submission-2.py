# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.globalSum = float("-inf")
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.globalSum = max(self.globalSum, max(left,0) + max(right,0) + root.val)
            return root.val + max(left, right, 0)
        dfs(root)
        return self.globalSum

            
