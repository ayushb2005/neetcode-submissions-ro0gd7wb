class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        find a 1 add it to a visited set
        then we check left, right, up, down if 1 add to stack toVisit
        then we check whicever direction and apply the same and add those 
        into a visited set everytime we pop off stack. Once everything 
        off stack is popped off continue going through the lists 
        checking if there is a 1 AND it is not in a visited set

        '''
        visitedSet = set()
        visitStack = [] #append, pop
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if(grid[row][col] == "1" and (row,col) not in visitedSet):
                    islands += 1
                    visitStack.append((row,col))
                    #DFS
                    while(visitStack):
                        remove = visitStack.pop()
                        visitedSet.add(remove)
                        self.checkNeighbors(grid, remove[0], remove[1], visitedSet, visitStack)
                        #check neighbors
                        #check bounds, land, not visited
        return islands
                        
    def checkNeighbors(self, grid, row, col, visitedSet, visitStack):
        #[row+1][col], [row-1][col], [row][col+1], [row][col-1]
        if(0 <= row+1 < len(grid) and 0 <= col < len(grid[0]) \
        and grid[row+1][col] == "1" and (row+1, col) not in visitedSet):
            visitStack.append((row+1,col))
        if(0 <= row-1 < len(grid) and 0 <= col < len(grid[0]) \
        and grid[row-1][col] == "1" and (row-1, col) not in visitedSet):
            visitStack.append((row-1,col))
        if(0 <= row < len(grid) and 0 <= col+1 < len(grid[0]) \
        and grid[row][col+1] == "1" and (row, col+1) not in visitedSet):
            visitStack.append((row,col+1))
        if(0 <= row-1 < len(grid) and 0 <= col-1 < len(grid[0]) \
        and grid[row][col-1] == "1" and (row, col-1) not in visitedSet):
            visitStack.append((row,col-1))
        
            

