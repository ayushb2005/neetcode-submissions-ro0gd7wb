class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        input1Map = {}
        input2Map = {}

        for i in s:
            if i in input1Map:
                input1Map[i] += 1
            else:
                input1Map[i] = 1
        for i in t:
            if i in input2Map:
                input2Map[i] += 1
            else:
                input2Map[i] = 1
        return input1Map == input2Map