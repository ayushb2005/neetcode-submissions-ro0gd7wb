"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        create a clone of every element, use the hashmap to keep track
        of the clones that are created
        because val 1 -> 2, but 2 -> 1, need to make sure we do not create
        another copy of 1, and instead just check hte hashmap if it exists
        '''
        if node is None:
            return 
        hashMap = {} #key: original node, value: cloned node
        clonedNode = Node(node.val, [])
        hashMap[node] = clonedNode
        if not node.neighbors:
            return clonedNode
        stack = [node]
        while(stack):
            removeNode = stack.pop()
            for i in removeNode.neighbors:
                if(i not in hashMap):
                    cloneNode = Node(i.val, [])
                    hashMap[i] = cloneNode
                    hashMap[removeNode].neighbors.append(hashMap[i])
                    stack.append(i)
                else:
                    hashMap[removeNode].neighbors.append(hashMap[i])
        return hashMap[node]

        




        

