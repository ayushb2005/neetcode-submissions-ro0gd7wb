class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1

        #0 1 2 3
        #3 0 1 2
        # 5 4 3 2
        while(left < right):
            middle = (left + right) // 2
            if(nums[middle] > nums[right]):
                left = middle + 1
            else:
                right = middle
        return nums[left]