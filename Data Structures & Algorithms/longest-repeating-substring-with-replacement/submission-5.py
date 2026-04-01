class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        sliding window 
        start with LR initialized with 0
        hashmap with all 26 letters of the alphabet
        for that sliding window add inside a hashmap the count of a char
        subtract windowlength - most seen char in that window
        ensure that the window is <= k
        if it isnt then move L otherwise keep moving right
        track the max of the biggest window
        '''
        maxTracker = -1
        left = 0
        right = 0
        hashMap = {} 
        for i in range(len(s)):
            if s[i] not in hashMap:
                hashMap[s[i]] = 1
            else:
                hashMap[s[i]] += 1
            windowLength = i - left + 1
            kComparison = windowLength - max(hashMap.values())
            if(kComparison <= k):
                maxTracker = max(maxTracker, windowLength)
            else:
                hashMap[s[left]] -= 1
                left += 1
        return maxTracker
            

