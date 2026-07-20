class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        maxSum = -100000000
        for i in nums:
            cur += i
            maxSum = max(maxSum, cur)
            if cur < 0:
                cur = 0
        return maxSum
        
