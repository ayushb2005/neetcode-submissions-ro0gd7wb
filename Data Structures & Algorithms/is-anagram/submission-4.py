class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if(len(s) != len(t)):
        #     return False
        # lst1 = [0]*26
        # lst2 = [0]*26
        # for i in range(len(s)):
        #     idx1 = ord('a')-ord(s[i])
        #     idx2 = ord('a')-ord(t[i])
        #     lst1[idx1] += 1
        #     lst2[idx2] += 1
        # if(lst1 == lst2):
        #     return True
        # return False
        map1, map2 = {},{}
        for i in s:
            if i not in map1:
                print(map1)
                map1[i] = 0
            else:
                map1[i] += 1
        for i in t:
            if i not in map2:
                map2[i] = 0
            else:
                map2[i] += 1    
        return map1 == map2  

        
        