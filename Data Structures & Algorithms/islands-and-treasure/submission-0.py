class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] == 0):
                    queue.append((i,j))
        counter = 0
        while(queue):
            length = len(queue)
            for _ in range(length):
                pop = queue.popleft()
                grid[pop[0]][pop[1]] = counter 
                self.check(grid, queue, pop[0], pop[1], counter)
            counter += 1

    def check(self, grid, queue, i, j, counter):
        sides = [(1,0), (-1,0), (0,1), (0,-1)]
        for side in sides:
            x = side[0] + i
            y = side[1] + j
            if(0<= x < len(grid) and 0<= y < len(grid[i]) and \
            grid[x][y] == 2**31-1):
                grid[x][y] = counter + 1
                queue.append((x,y))