class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        self.curSum = 0 
        array = []
        res = []
        #1,2,2
        def dfs(i):
            if self.curSum == target:
                array.append(res.copy())
                return
            if self.curSum > target or i+1 > len(candidates):
                return
            res.append(candidates[i])
            self.curSum += candidates[i]
            dfs(i+1)
            self.curSum -= res.pop()
            
            cur = i
            while cur+1 < len(candidates) and candidates[cur] == candidates[cur+1]:
                cur += 1
            dfs(cur+1)
        dfs(0)
        return array




            