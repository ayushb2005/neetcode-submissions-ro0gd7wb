class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hashset = set(tuple(wordDict))
        dpArray = [False] * (len(s)+1)
        dpArray[0] = True
        for i in range(len(s)+1):
            for j in range(i):
                if dpArray[j] and s[j:i] in hashset:
                    dpArray[i] = True
                    break
        print(dpArray)
        return dpArray[-1]