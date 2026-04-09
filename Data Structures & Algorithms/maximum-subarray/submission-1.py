class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        keep a sum 
        '''
        maxSum = nums[0]
        for i in range(len(nums)):
            sumFromI = 0
            for j in range(i, len(nums)):
                sumFromI += nums[j]
                maxSum = max(maxSum, sumFromI)
        return maxSum
