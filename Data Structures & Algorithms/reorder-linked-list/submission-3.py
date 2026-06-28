# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondHalf = slow.next
        slow.next = None

        #flip links for second half
        cur = secondHalf
        prev = None

        while(cur):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        #2 4 
        #8 6
        # dummyNode = ListNode()
        # dummy = dummyNode
        # cur = head
        # cur2 = prev
        # while(cur):
        #     dummy.next = cur
        #     dummy = dummy.next
        #     cur = cur.next
        #     if(cur2):
        #         dummy.next = cur2
        #         cur2 = cur2.next
        #         dummy = dummy.next
        # head = dummyNode.next

        first = head
        second = prev
        while(second):
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
        return None



        
        
        

