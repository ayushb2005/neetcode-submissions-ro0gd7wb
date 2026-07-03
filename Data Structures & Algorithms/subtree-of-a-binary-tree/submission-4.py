# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return False
        if root is None and subRoot is None:
            return True
        
        def isTree(p, q):
            self.boolean = True
            def dfs(p,q):
                if p is None and q is None:
                    return True
                if (p is None and q is not None) or p is not None and q is None:
                    self.boolean = False
                    return False
                if(p.val != q.val):
                    self.boolean = False
                    return False
                return dfs(p.left, q.left) and dfs(p.right, q.right)
            dfs(p,q)
            return self.boolean
        
        if(root.val == subRoot.val and isTree(root, subRoot)):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            
            