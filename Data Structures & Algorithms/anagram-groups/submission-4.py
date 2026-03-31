class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #loop through the strings
        #create a sorted hash of each string and then value is a list of strings
        #time complexity: o(n*k)
        mapStr = {}
        for i in strs:
            sortedLst = [0]*26
            for j in i:
                sortedLst[ord(j)-ord('a')] += 1
            hashString = ""
            print(sortedLst)
            for j in range(len(sortedLst)):
                hashString += chr(97+j)+str(sortedLst[j])
            if hashString in mapStr:
                mapStr[hashString].append(i)
            else:
                mapStr[hashString] = [i]
        print(mapStr.values())
        return list(mapStr.values())