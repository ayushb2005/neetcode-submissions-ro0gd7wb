class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j] == word[0]):
                    if len(word) == 1:
                        return True
                    seenSet = {(i,j)}
                    def dfs(i, j, index, board, seenSet):
                        if index == len(word):
                            return True
                        check = [(1,0), (-1,0), (0,-1), (0,1)]
                        for dir in check:
                            x = dir[0] + i
                            y = dir[1] + j
                            if (0<= x < len(board) and 0<= y < len(board[0]) \
                            and board[x][y] == word[index] and (x,y) not in seenSet):
                                seenSet.add((x,y))
                                if dfs(x,y, index+1, board, seenSet):
                                    return True
                                seenSet.remove((x,y))
                        return False
                    if dfs(i, j, 1, board, seenSet):
                        return True
        return False

                            
                        

                        

