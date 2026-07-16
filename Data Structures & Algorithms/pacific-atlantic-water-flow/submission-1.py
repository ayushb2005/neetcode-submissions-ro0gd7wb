class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #pacific
        stack = []

        pacific_visit = set()
        for j in range(len(heights[0])):
            stack.append((0,j))
        for i in range(len(heights)):
            stack.append((i, 0))
        while(stack):
            i,j = stack.pop()
            pacific_visit.add((i,j))
            self.check(stack, i, j, pacific_visit, heights)
        stack = []
        atlantic_visit = set()
        for i in range(len(heights)):
            stack.append((i, len(heights[0])-1))
        for j in range(len(heights[len(heights)-1])):
            stack.append((len(heights)-1, j))
        print(stack)
        while(stack):
            i,j = stack.pop()
            atlantic_visit.add((i,j))
            self.check(stack, i, j, atlantic_visit, heights)
        return list(atlantic_visit & pacific_visit)

    def check(self, stack, i, j, seenSet, heights):
        sides = [(1,0), (-1,0), (0,1), (0,-1)]
        for side in sides:
            x = i + side[0] 
            y = j + side[1]
            if(0 <= x < len(heights) and 0<= y < len(heights[0]) \
            and (x,y) not in seenSet and heights[x][y] >= heights[i][j]):
                stack.append((x,y))

        
