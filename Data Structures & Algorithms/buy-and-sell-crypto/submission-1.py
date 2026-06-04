class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        current = 1000
        for i in range(len(prices)):
            if(current > prices[i]):
                current = prices[i]
            if(prices[i] > current):
                profit = max(prices[i] - current, profit)
        return profit