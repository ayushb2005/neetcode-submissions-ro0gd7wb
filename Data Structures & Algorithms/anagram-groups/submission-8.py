class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for i in strs:
            stringCount = [0]*26
            for letter in i:
                stringCount[ord(letter) - ord('a') ] += 1
            print(stringCount)
            toTuple = tuple(stringCount)
            if toTuple in hashMap:
                hashMap[toTuple].append(i)
            else:
                hashMap[toTuple] = [i]
        return list(hashMap.values())