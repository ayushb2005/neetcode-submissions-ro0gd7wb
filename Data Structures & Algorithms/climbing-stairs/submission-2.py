class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        dp = [0]*(n+1)
        #0,1,2
        count = 0 
        for i in range(n, -1, -1):
            if i == n:
                dp[n] = 1
            elif(i == n-1):
                dp[n-1] = 1
            else:
                dp[i] = dp[i+1] + dp[i+2]
        return dp[0]