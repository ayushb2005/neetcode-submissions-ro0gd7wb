class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        start from the end keep finding a value until we can reach the next
        goalpost

        '''
        reach = None
        for i in range(len(nums)-1, -1, -1):
            if reach == None:
                reach = i
                print(reach)
            else:
                if nums[i] + i >= reach:
                    reach = i
                    if i ==0:
                        return True
                if i==0 and nums[i] + i != reach:
                    return False
        return True

