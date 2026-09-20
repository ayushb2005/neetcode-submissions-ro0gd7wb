class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dpArray = [0] * (len(nums))
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                dpArray[i] = 1
            elif i == len(nums) - 2:
                if nums[i] < nums[i+1]:
                    dpArray[i] = max(1, 1 + dpArray[i+1])
                else:
                    dpArray[i] = 1
            else:
                dpArray[i] = 1
                for j in range(i+1, len(nums)):
                    if nums[i] < nums[j]:
                        dpArray[i] = max(dpArray[i], 1+dpArray[j])
            # print(dpArray)
        return max(dpArray)

                
                
