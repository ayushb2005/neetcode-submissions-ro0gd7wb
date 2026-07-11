class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue = deque()
        border = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j] == "O"):
                    if(j == 0 or j == len(board[i]) - 1):
                        queue.append((i,j))
                        border.add((i,j))
                    if(i == 0 or i == len(board) - 1):
                        queue.append((i,j))
                        border.add((i,j))
           
        while(queue):
            length = len(queue)
            for i in range(length):
                pop = queue.popleft()
                self.check(board, border, pop[0], pop[1], queue)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j] == "O" and (i,j) not in border):
                    board[i][j] = "X"
        return

    def check(self, board, border, i, j, queue):
        sides = [(1,0), (-1,0), (0,-1), (0,1)]
        for side in sides:
            x = side[0] + i
            y = side[1] + j
            if(0<=x<len(board) and 0<=y<len(board[i]) and \
            board[x][y] == "O" and (x,y) not in border):
                border.add((x,y))
                queue.append((x,y))
    