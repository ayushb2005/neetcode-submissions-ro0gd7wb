class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        maxString = 0
        counter = 0
        left = 0
        for i in range(len(s)):
            if(s[i] in hashMap):
                hashMap[s[i]] += 1
            else:
                hashMap[s[i]] = 1
            counter += 1
            while(i - left - max(hashMap.values()) + 1 > k):
                hashMap[s[left]] -= 1
                left += 1
                counter -= 1
            maxString = max(maxString, counter)
        return maxString