class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        index = 0 
        total = 0

        for i in range(len(gas)):
            if total + gas[i] - cost[i] < 0:
                index = i+1
                total = 0
            else:
                total += gas[i] - cost[i]
        return index
