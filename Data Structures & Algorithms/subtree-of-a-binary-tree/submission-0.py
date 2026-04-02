# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(subRoot is None):
            return True
        if(root is None):
            return False
        if(self.sameTree(root, subRoot)):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    #have a helper function to tell us if two treees are the same
    def sameTree(self, s, q):
        if(s is None and q is None):
            return True
        elif(s is None and q is not None or (s is not None and q is None)):
            return False
        elif(s.val != q.val):
            return False
        return self.sameTree(s.left, q.left) and self.sameTree(s.right, q.right)
        