# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        [1,2,3,4,5,6]
        at most only half 
        get n, 
        start from 0, alternate between start counter and end
        keep a prev for both 
        get the first n on a queue, and the other side on a stack

        fast pointer, slow pointer
        use this to find where 
        the middle is so that everything after is reversed 
        1 2 3 4 5
        s = 3, f = 5.next = null
        1 2 3 4 5 6
        s = 3, f = 6
        '''
        #find middle with slow, fast pointer
        sp = head
        fp = head.next
        while(fp and fp.next):
            sp = sp.next
            fp = fp.next.next
        
        #flip second
        prev = None
        second = sp.next
        sp.next = None
        while(second):
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        #combine
        first = head
        second = prev
        while(second):
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        

        

