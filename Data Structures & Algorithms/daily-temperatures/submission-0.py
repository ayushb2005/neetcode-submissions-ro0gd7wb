class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        add until a number larger than the top of the stack appears
        keep popping until we find a spot it can be in
        in the end check if stack is not empty, we will empty it and give
        the remaining numbers a 0
        '''
        resultStack = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while(stack and temperatures[i] > temperatures[stack[-1]]):
                resultStack[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        for i in stack:
            resultStack[i] = 0
        return resultStack
        