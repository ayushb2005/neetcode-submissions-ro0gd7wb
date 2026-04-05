# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visitSet = set()
        curr = head
        while(curr):
            visitSet.add(curr)
            if(curr.next in visitSet):
                return True
            curr = curr.next
        return False