class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        keep a sum 
        '''
        # maxSum = nums[0]
        # for i in range(len(nums)):
        #     sumFromI = 0
        #     for j in range(i, len(nums)):
        #         sumFromI += nums[j]
        #         maxSum = max(maxSum, sumFromI)
        # return maxSum
        l = 0
        r = 0
        maxSum = nums[0] 
        curSum = 0
        for i in nums:
            if(curSum < 0):
                curSum = 0
            curSum += i
            maxSum = max(maxSum, curSum)
        return maxSum
