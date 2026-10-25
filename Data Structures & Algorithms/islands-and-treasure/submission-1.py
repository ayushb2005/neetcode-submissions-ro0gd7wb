class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        deq = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    deq.append((i,j))
        
        while deq:
            deqNum = len(deq)
            for i in range(deqNum):
                x,y = deq.popleft()
                self.check(x,y,grid,deq)
        
    def check(self, x,y,grid, deq):
        check = [(1,0), (-1,0), (0,1), (0,-1)]

        for i,j in check:
            x1 = x + i
            y1 = y + j

            if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[x1]) and grid[x1][y1] == (2**31 - 1):
                grid[x1][y1] = grid[x][y] + 1
                deq.append((x1,y1))
    