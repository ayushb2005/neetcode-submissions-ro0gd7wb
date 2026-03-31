class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1 = set()
        maxNum = 0
        l=0
        for r in range(len(s)):
            while(s[r] in set1):
                set1.remove(s[l])
                l+=1
            set1.add(s[r])
            maxNum = max(maxNum, r-l+1)
        return maxNum
