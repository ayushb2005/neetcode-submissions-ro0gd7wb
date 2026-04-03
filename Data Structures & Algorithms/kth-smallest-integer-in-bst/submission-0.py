# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        inorder traversal, append to array, then just return k index
        inorder, left, root, right which means that i will be going in sorted 
        order and i will keep a count that i will increment at every 
        number that i visit, if the count is = k then i will just 
        return the node.val
        '''
        stack = []
        curr = root
        #append and pop from the back, as the front
        count = 0
        while(curr or stack):
            while(curr):
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            count += 1
            if(count == k):
                return curr.val
            curr = curr.right
        return count
            
        # self.count = 0 
        # def dfs(root):
        #     if(root.left):
        #         return dfs(root.left)
        #     self.count += 1
        #     if(count == k):
        #         return root.val
        #     if(root.right):
        #         return dfs(root.right)
        #     return self.count
        # return dfs(root)
            


