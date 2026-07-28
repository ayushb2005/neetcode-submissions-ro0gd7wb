class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        cur = []
        array = []
        hashset = set()
        def dfs(i):
            if i >= len(nums):
                if tuple(cur) not in hashset:
                    hashset.add(tuple(cur))
                    array.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(i+1)
            
            cur.pop()
            dfs(i+1)
        dfs(0)
        return array
            