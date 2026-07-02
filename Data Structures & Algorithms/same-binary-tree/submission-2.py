# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.boolean = True
        def dfs(p, q):
            if p is None and q is None:
                return True
            if (p is None and q is not None) or (p is not None and q is None):
                self.boolean = False
                return False
            if(p.val != q.val):
                self.boolean = False
                return False
            dfs(p.left, q.left)
            dfs(p.right, q.right)
        dfs(p,q)
        return self.boolean

        