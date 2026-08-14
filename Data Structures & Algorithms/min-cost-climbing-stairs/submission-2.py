class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*(len(cost))

        # def dfs(i): 
        #     if i >= len(cost):
        #         return 0
        #     if dp[i] != 0:
        #         return dp[i]
        #     dp[i] = cost[i] + min(dfs(i+1), dfs(i+2))
        #     return dp[i]
        # dfs(0)
        # return min(dp[0], dp[1])

        for i in range(len(cost)-1, -1, -1):
            if i == len(cost)-1 or i == len(cost) - 2:
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        return min(dp[0], dp[1])