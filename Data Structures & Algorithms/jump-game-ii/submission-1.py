class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        l = 0
        r = 0
        minJump = 0
        while(r < len(nums) - 1):
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, nums[i] + i)
            l = r+1
            r = farthest
            minJump += 1
        return minJump