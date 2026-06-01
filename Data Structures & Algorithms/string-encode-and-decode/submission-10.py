class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for i in range(len(strs)):
            ret += str(len(strs[i])) + "#" + strs[i]
        print(ret)
        return ret
    def decode(self, s: str) -> List[str]:
        # 5#Hello5#World
        retArray = []
        i = 0
        while i < len(s):
            hashTag = s.index("#", i)
            length = int(s[i:hashTag])
            retArray.append(s[hashTag+1: length + hashTag+1])
            i =length + hashTag+ 1
        return retArray
