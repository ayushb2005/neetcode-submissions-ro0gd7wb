class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]] = i
            else:
                hashmap[s[i]] = i

        returnArray = []
        l, r = 0, 0
        lastIndex = 0
        while r < len(s):
            if hashmap[s[r]] > lastIndex:
                lastIndex = hashmap[s[r]]
            if lastIndex == r:
                returnArray.append(r-l+1)
                l = r + 1
            r +=1
            
        return returnArray
