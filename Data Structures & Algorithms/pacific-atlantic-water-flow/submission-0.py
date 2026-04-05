class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        flow from a to b if b is equal or lower
        split into two sets for the initial starts
        keep two sets one of pacific, and one of touching atlantic
        do DFS and check if any touching node if any touching node can flow 
        into it, if it can then add to stack to visit it and 
        add to visited set
        '''
        pacific = set()
        atlantic = set()

        #pacific top
        for i in range(len(heights[0])):
            stack = []
            stack.append((0,i))
            pacific.add((0,i))
            while(stack):
                value = stack.pop()
                self.checkAndAdd(value, heights, pacific, stack)

        #pacific left
        for i in range(len(heights)):
            #heights heights[i][0]
            stack = []
            stack.append((i,0))
            pacific.add((i,0))
            while(stack):
                value = stack.pop()
                self.checkAndAdd(value, heights, pacific, stack)
        #atlantic right
        for i in range(len(heights)):
            #heights heights[i][len(heights[0]-1)]
            stack = []
            stack.append((i,len(heights[0])-1))
            atlantic.add((i,len(heights[0])-1))
            while(stack):
                value = stack.pop()
                self.checkAndAdd(value, heights, atlantic, stack)
        #atlantic bottom
        for i in range(len(heights[len(heights)-1])):
            stack = []
            stack.append((len(heights)-1,i))
            atlantic.add((len(heights)-1,i))
            while(stack):
                value = stack.pop()
                self.checkAndAdd(value, heights, atlantic, stack)
        return list(pacific & atlantic)
    def checkAndAdd(self, valueTup, heights, oceanSet, stack):
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        for r,c in directions:
            if(0 <= valueTup[0]+r < len(heights) \
            and 0<= valueTup[1]+c < len(heights[0]) \
            and (valueTup[0]+r, valueTup[1]+c) not in oceanSet \
            and heights[valueTup[0]][valueTup[1]] <= \
            heights[valueTup[0]+r][valueTup[1]+c]):
                oceanSet.add((valueTup[0]+r, valueTup[1]+c))
                stack.append((valueTup[0]+r, valueTup[1]+c))

