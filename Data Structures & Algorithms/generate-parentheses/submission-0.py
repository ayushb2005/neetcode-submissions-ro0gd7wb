class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        array = []
        self.string = ""
        def dfs(open, close):
            if close > open:
                return 
            if len(self.string) == 2*n:
                array.append(self.string)
                return
            if(open < n):
                self.string += "("
                dfs(open+1, close)
                self.string = self.string[0:-1]
            if close < open:
                self.string += ")"
                dfs(open, close+1)
                self.string = self.string[0:-1]
        dfs(0,0)   
        return array


            