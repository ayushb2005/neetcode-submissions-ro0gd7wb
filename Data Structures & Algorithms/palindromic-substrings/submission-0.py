class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0 
        dpArray = []
        for i in range(len(s)):
            dpArray.append([0]*len(s))
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if j-i == 0:
                    dpArray[i][j] = True
                    counter += 1
                elif j-i == 1:
                    if s[i] == s[j]:
                        dpArray[i][j] = True
                        counter += 1
                    else:
                        dpArray[i][j] = False
                else:
                    if s[i] == s[j] and dpArray[i+1][j-1]:
                        counter += 1
                        dpArray[i][j] = True
                    else:
                        dpArray[i][j] = False
        return counter
                    

