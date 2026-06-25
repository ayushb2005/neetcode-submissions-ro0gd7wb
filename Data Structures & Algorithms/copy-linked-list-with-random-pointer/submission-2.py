"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        hashtable of all the nodes, then go back and add the random
        key: node #
        value: node
        old node: new node
        then create a LL after creating the map
        '''
        # print(head.next.random.val)
        if not head:
            return
        hashMap = {}
        cur = head
        while(cur):
            newNode = Node(cur.val)
            hashMap[cur] = newNode
            cur = cur.next
        cur = head
        while(cur):
            if(cur.next):
                hashMap[cur].next = hashMap[cur.next]
            if(cur.random):
                hashMap[cur].random = hashMap[cur.random]
            cur = cur.next
        # cur = head
        # while(cur):
        #     if(cur.random):
        #         hashMap[cur].random = hashMap[cur.random]
        #     cur = cur.next
        return hashMap[head]
                

