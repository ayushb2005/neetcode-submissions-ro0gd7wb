class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] == 2):
                    queue.append((i,j))
                if(grid[i][j] == 1):
                    fresh += 1
        minute = 0
        while(queue and fresh > 0):
            length = len(queue)
            for _ in range(length):
                pop = queue.popleft()
                fresh = self.check(queue, grid, pop[0], pop[1], fresh)
            minute += 1
        if(fresh > 0):
            return -1
        
        return minute

    def check(self, queue, grid, i, j, fresh):
        sides = [(1,0), (-1,0), (0,1), (0,-1)]
        for side in sides:
            x = side[0] + i
            y = side[1] + j
            if(0<=x<len(grid) and 0<=y<len(grid[i]) \
            and grid[x][y] == 1):
                queue.append((x,y))
                grid[x][y] = 2
                fresh -= 1
        return fresh