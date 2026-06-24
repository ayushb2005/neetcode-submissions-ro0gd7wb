# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # length = 0 
        # cur = head
        # while(cur):
        #     cur = cur.next
        #     length += 1
        # print(length-n)
        # prev = None
        # counter = 0
        # cur = head
        # dummy = ListNode()
        # start = dummy
        # while(cur):
        #     if(counter == length-n):
        #         if(prev is None):
        #             return cur.next
        #         prev.next = cur.next
        #         return start.next
        #     dummy.next = cur
        #     dummy = dummy.next
        #     prev = cur
        #     cur = cur.next
        #     counter += 1
        # return start.next

        '''
        start slow, fast at dummy node
        move fast n+1 spots away
        distance between slow and fast becomes n+1
        '''
        dummy = ListNode(0, head)
        right = dummy
        left = dummy
        counter = 0
        while(right and counter < n+1):
            counter += 1
            right = right.next
        
        while(right):
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next


