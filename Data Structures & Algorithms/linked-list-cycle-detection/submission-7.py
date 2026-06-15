# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # hashSet = set()

        # curr = head
        # while(curr):
        #     if(curr in hashSet):
        #         return True
        #     else:
        #         hashSet.add(curr)
        #         curr = curr.next

        # return False
        # if(head is None):
        #     return False
        # slow = head
        # fast = head.next
        # while(slow != fast):
        #     slow = slow.next
        #     if(fast is None or fast.next is None):
        #         return False
        #     else:
        #         fast = fast.next.next
        #     if(slow == None and fast == None):
        #         return False
        # return True
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                return True
        return False


