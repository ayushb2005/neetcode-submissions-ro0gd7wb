class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashMap = {}
        for i in s1:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1
        for i in range(len(s2)):
            hashMap2 = {}
            if(i+len(s1) <= len(s2)):
                left = i
                while(left < i + len(s1)):
                    if(s2[left] in hashMap2):
                        hashMap2[s2[left]] += 1
                    else:
                        hashMap2[s2[left]] = 1
                    left += 1
                if(hashMap2 == hashMap):
                    return True
        return False

