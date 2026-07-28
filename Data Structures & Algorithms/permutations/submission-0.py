class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        array = []
        path = []
        used = [False] * len(nums) 
        print(used)
        def dfs():
            if len(path) == len(nums):
                array.append(path.copy())
                return
            for j in range(len(used)):
                if not used[j]:
                    path.append(nums[j])
                    used[j] = True
                    dfs()
                    used[j] = False
                    path.pop()
                    
        dfs()
        return array
        