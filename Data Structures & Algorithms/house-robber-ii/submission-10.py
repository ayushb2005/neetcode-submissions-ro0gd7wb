class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp1 = [0]*(len(nums))
        dp2 = [0]*(len(nums))


        for i in range(len(nums)-1, 0, -1):
            if i == len(nums) -1:
                dp1[i] = nums[i]
            elif i == len(nums) - 2:
                dp1[i] = max(nums[i],dp1[i+1])
            else:
                dp1[i] = max(nums[i] + dp1[i+2], dp1[i+1])
        print(dp1)
        for i in range(len(nums)-2, -1, -1):
            print(nums[i])
            if i == len(nums) - 2:
                dp2[i] = nums[i]
            elif i == len(nums)-3:
                dp2[i] = max(nums[i], dp2[i+1])
            else:
                dp2[i] = max(nums[i] + dp2[i+2], dp2[i+1])
        print(dp2)
        return max(dp1[1], dp2[0])

        