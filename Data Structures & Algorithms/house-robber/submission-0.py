class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        [2,9,8,3,6]
        build left to right
        dp[0] = 2
        dp[1] = max(2,9)
        dp[2] = max(2+8,9)
        dp[3] = max(10, )
        '''
        dp = [0]*len(nums)
        maxNum = 0
        for i in range(len(nums)):
            if(i == 0):
                dp[0] = nums[i]
                maxNum = nums[i]
            else:
                if(i-2 >= 0):
                    maxNum = max(nums[i] + dp[i-2], maxNum)
                    dp[i] = maxNum
                else:
                    maxNum = max(nums[i], maxNum)
                    dp[i] = maxNum
        return dp[len(nums)-1]
