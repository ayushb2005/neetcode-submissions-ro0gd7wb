class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        increasing monotonic stack
        keep adding to the stack with the index and value until we find a value smaller than the top 
        of the stack, then at that point we keep popping and update max if needed
        '''
        stack = []
        maxRectangle = 0
        for i in range(len(heights)):
            start = i
            while(stack and heights[i] < stack[-1][1]):
                start = stack[-1][0]
                value = stack.pop()
                maxRectangle = max(maxRectangle, (i-value[0]) * value[1])
            stack.append((start,heights[i]))

        for i in range(len(stack)-1, -1, -1):
            maxRectangle = max(maxRectangle, (len(heights) - stack[i][0]) * stack[i][1])

        return maxRectangle

        