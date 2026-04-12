# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        cur = dummy
        while(l1 or l2 or carry):
            v1 = 0
            if l1:
                v1 = l1.val
            v2 = 0
            if l2:
                v2 = l2.val
            val = v1 + v2 + carry
            carry = val // 10 
            remainder = val % 10
            newNode = ListNode(remainder)
            cur.next = newNode
            cur = newNode

            if(l1):
                l1 = l1.next
            if(l2):
                l2 = l2.next
        return dummy.next

