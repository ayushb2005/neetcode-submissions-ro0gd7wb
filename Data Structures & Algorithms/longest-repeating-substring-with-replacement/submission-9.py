class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}

        left = 0
        curMax = 0
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]] += 1
            else:
                hashmap[s[i]] = 1
            if i - left + 1 - max(hashmap.values()) > k:
                hashmap[s[left]] -= 1
                left += 1
            curMax = max(curMax, i-left+1)
        return curMax