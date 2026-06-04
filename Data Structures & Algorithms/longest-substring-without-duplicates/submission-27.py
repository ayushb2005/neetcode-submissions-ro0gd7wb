class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        left = 0 
        maxString = 0
        counter = 0 
        for i in range(len(s)):
            while(s[i] in hashSet):
                hashSet.remove(s[left])
                left += 1
                counter -= 1
            else:
                counter += 1
                maxString = max(counter, maxString)
                hashSet.add(s[i])
        return maxString
                