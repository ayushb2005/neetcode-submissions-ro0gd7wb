"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        self.hashmap = {}
        seen = set()
        
        def dfs(node):
            if node in seen :
                return
            if node not in self.hashmap:
                newNode = Node(node.val, [])
                self.hashmap[node] = newNode 
            for i in node.neighbors:
                if i in self.hashmap:
                    self.hashmap[node].neighbors.append(self.hashmap[i])
                else:
                    newNode = Node(i.val, [])
                    self.hashmap[node].neighbors.append(newNode)
                    self.hashmap[i] = newNode
                seen.add(node)
                dfs(i)
        dfs(node)
        return self.hashmap[node]

        
