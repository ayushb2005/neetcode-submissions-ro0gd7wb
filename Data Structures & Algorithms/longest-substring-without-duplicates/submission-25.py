class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        starting with z then just move the right pointer and append to a set
        keep a maxCounter if that letter is in the set then 
        keep moving left until its valid
        '''
        left = 0 
        setSubStr = set()
        maxCounter = 0
        for i in range(len(s)):
            if(s[i] not in setSubStr):
                setSubStr.add(s[i])
                maxCounter = max(maxCounter, len(setSubStr))
            else:
                while(left < i and s[i] in setSubStr):
                    setSubStr.remove(s[left])
                    left += 1
                setSubStr.add(s[i])
        return maxCounter
