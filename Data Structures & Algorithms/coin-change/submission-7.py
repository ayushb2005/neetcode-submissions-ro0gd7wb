class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dpArray = [float("inf")] * (amount+1)
        dpArray[0] = 0
        for i in range(1, amount+1):
            minimum = 1000000000
            for coin in coins:
                if i == coin:
                    dpArray[i] = 1
                    break
                else:
                    if i - coin >= 0:
                        if dpArray[i-coin] != 0:
                            minimum = min(minimum, dpArray[i-coin]+1)
                if minimum == 1000000000:
                    dpArray[i] = 0
                else:
                    dpArray[i] = minimum
            # print(dpArray)
        if dpArray[amount] == 0:
            return -1
        return dpArray[amount]
                    
        

