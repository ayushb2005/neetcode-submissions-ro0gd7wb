class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Linked List cycle problem
        take a fast and slow pointer
        keep moving them until they intersect 
        then take a new slow pointer and see where this new slow pointer and original one intersect
        '''
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if(slow == fast):
                break
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if(slow == slow2):
                return slow
        return 
