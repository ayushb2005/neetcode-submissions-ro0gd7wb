class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        moves end to start -1 -> 0, everything moves 1 index forward
        we have to find the biggest number as next to it will be the 
        smallest number
        6 1 2 3 4 5
        5 6 1 2 3 4
        4 5 6 1 2 3
        3 4 5 6 1 2
        1 2 7 8 9 30
        30 1 2 7 8 9
        9 30 1 2 7 8
        8 9 30 1 2 7
        7 8 9 30 1 2

        1 2 3 4 5 6
        middle is 2
        move to the side from bst with the least node between the middle
        '''
        left = 0
        right = len(nums)-1
        while(left < right):
            middle = (right+left)//2
            if(nums[middle] > nums[right]):
                left = middle + 1
            else:
                right = middle
        return nums[left]
