# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        take the sum
        remainder + both number
        then get % (remainder), // for rounded down sum
        '''
        remainder = 0
        dummy = ListNode()
        track = dummy
        cur1 = l1
        cur2 = l2
        while(cur1 or cur2 or remainder):
            val1 = 0
            if(cur1):
                val1 = cur1.val
            val2 = 0
            if(cur2):
                val2 = cur2.val

            add = val1 + val2 + remainder
            remainder = add // 10
            digit = add % 10
            node = ListNode(digit)
            track.next = node

            track = track.next
            if(cur1):
                cur1 = cur1.next
            if(cur2):
                cur2 = cur2.next

        return dummy.next

            