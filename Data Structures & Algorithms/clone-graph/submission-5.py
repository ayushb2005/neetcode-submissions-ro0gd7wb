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
            return 
        if not node.neighbors:
            return Node(None, [])
        seenSet = set()
        hashmap = {}
        def dfs(node):
            if node in seenSet:
                return 
            seenSet.add(node)
            if node not in hashmap:
                newNode = Node(node.val)
                hashmap[node] = newNode
            for neighbor in node.neighbors:
                if neighbor not in hashmap:
                    newNodeNeighbor = Node(neighbor.val)
                    hashmap[neighbor] = newNodeNeighbor
                hashmap[node].neighbors.append(hashmap[neighbor])
                dfs(neighbor)
            return
        
        for n in node.neighbors:
            dfs(n)
        return hashmap[node]
                    
            

