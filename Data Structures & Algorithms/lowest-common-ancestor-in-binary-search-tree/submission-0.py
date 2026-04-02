# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        current Node when traversing
        if node children ==p and ==q then return node
        or if node chilren where one is ==p or ==q but current node
        is equal to either p or q
        doing left subtree, if P is in left subtree
        '''
        if(p.val<root.val and q.val<root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif(p.val>root.val and q.val>root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        return root
        
        