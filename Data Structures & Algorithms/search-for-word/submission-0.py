class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        dfs with a character that matches, just do it twice
        '''
        visit = set()
        row = len(board)
        col = len(board[0])
        def dfs(r, c, i):
            if i == len(word):
                return True
            if(r < 0 or r >= row or c<0 or c>=col \
            or word[i] != board[r][c] or (r,c) in visit):
                return False
            visit.add((r,c))
            dir = [(0,1), (0,-1), (1,0), (-1,0)]
            res = False
            for r1,c1 in dir:
                if(dfs(r+r1, c+c1, i+1)):
                    res = True
                    break
            visit.remove((r,c))
            return res
        for r in range(row):
            for c in range(col):
                if(dfs(r,c,0)):
                    return True
        return False
        
            

