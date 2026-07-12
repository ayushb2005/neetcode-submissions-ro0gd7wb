class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue = deque()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j] == "O"):
                    if(j == 0 or j == len(board[i]) - 1 \
                    or i == 0 or i == len(board) - 1):
                        queue.append((i,j))
                        board[i][j] = "T"
           
        while(queue):
            pop = queue.popleft()
            self.check(board, pop[0], pop[1], queue)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j] == "O"):
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        return

    def check(self, board, i, j, queue):
        sides = [(1,0), (-1,0), (0,-1), (0,1)]
        for side in sides:
            x = side[0] + i
            y = side[1] + j
            if(0<=x<len(board) and 0<=y<len(board[i]) and \
            board[x][y] == "O"):
                board[x][y] = "T"
                queue.append((x,y))
    