# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        '''
        preorder traversal
        append to a string using dfs
        '''
        self.serStr = ""
        def dfs(root):
            if not root:
                self.serStr += "N,"
                return
            else:  
                self.serStr += f"{root.val},"
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        if(self.serStr[-1] == ","):
            self.serStr = self.serStr[:len(self.serStr)-1]
        print(self.serStr)
        return self.serStr
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or data[0] == "N":
            return None
        self.deserArr = data.split(',')
        self.index = 0

        def dfs():
            if(self.deserArr[self.index] == "N"):
                self.index += 1
                return None
            node = TreeNode(self.deserArr[self.index])
            self.index += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

            
        
        