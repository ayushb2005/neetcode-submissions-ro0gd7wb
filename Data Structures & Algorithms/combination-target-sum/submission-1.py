class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        array = []
        res = []
        self.curSum = 0

        def dfs(i):
            if(self.curSum == target):
                array.append(res.copy())
                return
            if self.curSum > target or i+1 > len(nums):
                return
            res.append(nums[i])
            self.curSum += nums[i]
            dfs(i)
            self.curSum -= res.pop()
            dfs(i+1)
        dfs(0)
        return array
