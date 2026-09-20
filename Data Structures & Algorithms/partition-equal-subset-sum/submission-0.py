class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        x = sum(nums)
        if x % 2 != 0:
            return False
        target = x//2
        dpArray = [False] * (target+1)
        dpArray[0] = True

        for num in nums:
            for i in range(target, num-1, -1):
                if dpArray[i-num]:
                    dpArray[i] = True
        return dpArray[target]
        