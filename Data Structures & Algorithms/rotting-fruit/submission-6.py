class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        freshOranges = 0

        deq = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    deq.append((i,j))
                elif grid[i][j] == 1:
                    freshOranges += 1

        while deq:
            deqSize = len(deq)
            for i in range(deqSize):
                x,y = deq.popleft()
                freshOranges = self.check(grid, x,y, deq, freshOranges)
            minutes += 1
        if freshOranges > 0:
            return -1
        if minutes == 0:
            return 0
        return minutes - 1
    def check(self, grid, x, y, queue, freshOranges):
        check = [(0,1), (1,0), (0,-1), (-1,0)]
        for i,j in check:
            print(i)
            x1 = x + i
            y1 = y + j
            if 0 <= x1 < len(grid) and 0<= y1 < len(grid[x]) and grid[x1][y1] == 1:
                grid[x1][y1] = 2
                queue.append((x1,y1))
                freshOranges -= 1
        return freshOranges

