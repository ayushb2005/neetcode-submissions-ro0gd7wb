class Solution:
    def trap(self, height: List[int]) -> int:
        #max height to the left
        #max height to the right

        left = 0 
        right = len(height) - 1
        maxLeft = 0 
        maxRight = 0
        maxWater = 0

        while(left < right):
            maxLeft = max(height[left], maxLeft)
            maxRight = max(height[right], maxRight)
            if(maxLeft < maxRight):
                if(maxLeft - height[left] >= 0):
                    maxWater += maxLeft - height[left]
                
                left += 1
            else:
                if(maxRight - height[right] >= 0):
                    maxWater += maxRight - height[right]
                right -= 1
        return maxWater
            
