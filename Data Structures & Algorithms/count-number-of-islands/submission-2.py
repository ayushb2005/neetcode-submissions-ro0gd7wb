class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] == "1" and (i,j) not in seen):
                    islands += 1
                    stack = [(i,j)]
                    while(stack):
                        value = stack.pop()
                        seen.add(value)
                        self.check(stack, value[0], value[1], seen, grid)
        return islands
    def check(self, stack, i, j, seen, grid):
        sides = [(1,0), (0,1), (-1,0), (0,-1)]
        for side in sides:
            x = side[0] + i
            y = side[1] + j
            if(0 <= x < len(grid) and 0 <= y < len(grid[i]) and \
            grid[x][y] == "1" and (x,y) not in seen):
                stack.append((x,y))
    

