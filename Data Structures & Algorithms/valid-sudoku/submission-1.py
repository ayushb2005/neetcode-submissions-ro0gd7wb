class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            hashSetRow = set()
            hashSetCol = set()
            for j in range(9):
                if(board[i][j] != "."):
                    if board[i][j] in hashSetRow:
                        return False
                    hashSetRow.add(board[i][j])
                if(board[j][i] != "."):
                    if board[j][i] in hashSetCol:
                        return False
                    hashSetCol.add(board[j][i])
           
        
        hashSet3 = {}
        for i in range(9):
            for j in range(9):
                if(board[i][j] != "."):
                    if (i//3,j//3) in hashSet3:
                        hashSet = hashSet3[(i//3,j//3)]
                        if(board[i][j] in hashSet):
                            return False
                        else:
                            hashSet.add(board[i][j])
                    else:
                        hashSet3[(i//3,j//3)] = set(board[i][j])
        print(hashSet3)
        return True