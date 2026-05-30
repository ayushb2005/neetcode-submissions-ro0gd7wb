class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #find element that doesn't have it-1 then create another loop to continue finding, use hashmap
        hashSet = set()
        for i in nums:
            hashSet.add(i)
        maxCounter = 0
        for i in hashSet:
            if i-1 not in hashSet:
                num = i
                counter = 1
                while(num + 1 in hashSet):
                    counter += 1
                    num += 1
                maxCounter = max(maxCounter, counter) 
        return maxCounter