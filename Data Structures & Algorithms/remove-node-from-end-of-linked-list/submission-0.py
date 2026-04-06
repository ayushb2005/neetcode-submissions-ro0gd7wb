# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        take the total length of the list, -n = position to remove
        '''
        curr = head
        llLength = 0
        while(curr):
            llLength+=1
            curr = curr.next
        positionRemove = llLength - n
        counter = 0
        curr = head
        prev = None
        while(curr):
            print(curr.val)
            if(counter == positionRemove):
                print()
                if(curr == head):
                    head = curr.next
                    return head
                else:
                    prev.next = curr.next
                    return head
            else:
                prev = curr
                curr = curr.next
                counter+=1
        return 