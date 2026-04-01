class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        two pointer question
        calculate an area 
        move the smaller height pointer
        and calculate the area and keep the max
        (right - left) * min(heightL, heightR)
        then keep a variable to keep track of the water
        '''

        left = 0
        right = len(heights) - 1
        maxWater = 0
        for i in range(len(heights)):
            currentArea = (right-left) * min(heights[left], heights[right])
            maxWater = max(maxWater, currentArea)
            if(heights[left] < heights[right]):
                left += 1
            else:
                right -= 1
        return maxWater
