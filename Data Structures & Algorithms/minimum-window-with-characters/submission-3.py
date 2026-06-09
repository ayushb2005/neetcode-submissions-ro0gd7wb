class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        go through the string and check if we need that character in t,
        then increment or add to s hashmap, check if they are equal if equal increment have += 1
        check have == need
        store that in a result with the substring and length

        start remvoing leftmost character until have != need
        remove from the current window 
        in doing so check if we need to change the have and the hashmap of s
        after that keep adding characters bc it is invalid from the right

        even if a character is >= doesnt change the have
        '''
        tMap = {}
        for i in t:
            if i in tMap:
                tMap[i] += 1
            else:
                tMap[i] = 1
        need = len(tMap)
        have = 0
        sMap = {}
        left = 0

        length = 1000
        substring = ""

        for i in range(len(s)):
            if(have < need):
                if(s[i] in tMap):
                    if(s[i] in sMap):
                        sMap[s[i]] += 1
                    else:
                        sMap[s[i]] = 1
                    if(sMap[s[i]] == tMap[s[i]]):
                        have += 1
                    if(have == need):
                        if(length > i - left + 1):
                            length = i - left + 1
                            substring = s[left:i+1]
            while(have == need):
                if s[left] in sMap:
                    sMap[s[left]] -= 1
                    if(sMap[s[left]] < tMap[s[left]]):
                        have -= 1
                if(length > i - left + 1):
                    length = i - left + 1
                    substring = s[left:i+1]
                left += 1
        return substring

                        

