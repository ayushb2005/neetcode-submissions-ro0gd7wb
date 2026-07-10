class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxIsland = 0 
        seen = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] == 1 and (i,j) not in seen):
                    stack = [(i,j)]
                    island = 0
                    while(stack):
                        value = stack.pop()
                        if value in seen:
                            continue
                        seen.add(value)
                        self.check(value[0], value[1], seen, stack, grid)
                        island += 1
                    maxIsland = max(maxIsland, island)
        return maxIsland
        
    def check(self, i, j, seen, stack, grid):
        sides = [(1,0), (-1,0), (0,1), (0,-1)]
        for side in sides:
            x = i + side[0]
            y = j + side[1]
            if(0<= x < len(grid) and 0<= y < len(grid[i]) and \
            grid[x][y] == 1 and (x,y) not in seen):
                stack.append((x,y))