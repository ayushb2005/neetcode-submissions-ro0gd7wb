class Solution:
    def numDecodings(self, s: str) -> int:
        
        dpArray = [0] * len(s)
        for i in range(len(s)):
            if i == 0:
                if s[i] == "0":
                    return 0
                else:
                    dpArray[i] = 1
            elif i == 1:
                if s[i] == "0" and int(s[i-1]) > 2:
                    return 0
                elif s[i] == "0" and 0 < int(s[i-1]) < 3:
                    dpArray[i] = 1
                elif s[i] == "0" and s[i-1] == "0":
                    return 0
                else:
                    if 10 <= int(s[i-1] + s[i]) <= 26:
                        dpArray[i] = 2
                    else:
                        dpArray[i] = 1
            else:
                if s[i] == "0" and int(s[i-1]) > 2:
                    return 0
                elif s[i] == "0" and 0 < int(s[i-1]) < 3:
                    dpArray[i] = dpArray[i-2]
                elif s[i] == "0" and s[i-1] == "0":
                    return 0
                else:
                    count = int(s[i-1] + s[i])
                    if 10 <= count <= 26:
                        dpArray[i] = dpArray[i-1] + dpArray[i-2]
                    else:
                        dpArray[i] = dpArray[i-1]
        print(dpArray)
        return dpArray[-1] 
            

