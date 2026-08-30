class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = []
        for i in range(len(s)):
            dp.append([0]*len(s))
        longest = 0
        string = (0,0)
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if j-i == 0:
                    dp[i][j] = True
                    if(longest < j-i+1):
                        longest = j-i+1
                        string = (i, j+1)
                elif j-i == 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        if(longest < j-i+1):
                            longest = j-i+1
                            string = (i, j+1)
                    else:
                        dp[i][j] = False
                else:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                        if(longest < j-i+1):
                            longest = j-i+1
                            string = (i, j+1)
                    else:
                        dp[i][j] = False
        return s[string[0]: string[1]]


