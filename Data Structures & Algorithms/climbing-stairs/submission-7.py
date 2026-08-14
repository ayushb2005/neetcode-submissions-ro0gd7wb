class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)

        # def dfs(i):
        #     if i > n:
        #         return 0    
        #     if i == n:
        #         return 1
        #     if dp[i] != 0:
        #         return dp[i]
        #     dp[i] = dfs(i+1) + dfs(i+2)
        #     return dp[i]
        # return dfs(0)

        for i in range(n, -1, -1):
            print(i)
            if i == n or i == n-1:
                dp[i] = 1
            else:
                dp[i] = dp[i+1] + dp[i+2]
        return dp[0]