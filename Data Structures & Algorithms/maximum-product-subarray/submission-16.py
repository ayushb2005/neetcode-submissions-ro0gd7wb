class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur = nums[0]
        maxProd = nums[0]
        minProd = nums[0]
        totalMax = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == 0:
                totalMax = max(nums[i],totalMax, maxProd)
                maxProd = 1
                minProd = 1
            else:
                oldMaxProd = maxProd
                oldMin = minProd
                maxProd = max(nums[i], nums[i] * oldMaxProd, nums[i] * oldMin)
                minProd = min(nums[i], nums[i] * oldMin, nums[i] * oldMaxProd)
                totalMax = max(totalMax, maxProd, minProd) 
        return totalMax

            

            
