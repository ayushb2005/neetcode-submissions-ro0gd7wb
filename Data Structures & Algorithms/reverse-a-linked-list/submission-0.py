# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        stack to do this, keep appending until end then just 
        pop off one at a time, and make the new links
        '''
        if(not head):
            return 
        stack = []
        cur = head
        while(cur):
            stack.append(cur)
            cur = cur.next
        prev = stack.pop()
        head = prev
        while(stack):
            popped = stack.pop()
            prev.next = popped
            prev = popped
        prev.next = None
        return head

