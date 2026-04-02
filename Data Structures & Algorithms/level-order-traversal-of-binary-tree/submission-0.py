# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root is None):
            return []
        outputArray = [[root.val]]
        q = deque([root])

        while(q):
            level = len(q)
            levelArray = []
            for i in range(level):
                node = q.popleft()
                if(node.left):
                    q.append(node.left)
                    levelArray.append(node.left.val)
                if(node.right):
                    q.append(node.right)
                    levelArray.append(node.right.val)
            if(levelArray):
                outputArray.append(levelArray)
        return outputArray
