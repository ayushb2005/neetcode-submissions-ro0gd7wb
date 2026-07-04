# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        deq = deque([root])
        bfsArray = []
        while(deq):
            length = len(deq)
            array = []
            for i in range(length):
                node = deq.popleft()
                if(node.left):
                    deq.append(node.left)
                if(node.right):
                    deq.append(node.right)
                if(i == length - 1):
                    bfsArray.append(node.val)
        return bfsArray
        #         array.append(node.val)
        #     bfsArray.append(array)
        # print(bfsArray)
        # outputArray = []
        # for i in range(len(bfsArray)):
        #     outputArray.append(bfsArray[i][len(bfsArray[i])-1])
        # return outputArray

