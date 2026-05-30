class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i in nums:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1
        bucketSort = []
        for i in range(len(nums)):
            bucketSort.append([])
        for i in hashMap:
            bucketSort[hashMap[i]-1].append(i)
        returnArray = []
        counter = 0
        for i in range(len(bucketSort)-1, -1, -1):
            for j in range(len(bucketSort[i])-1, -1, -1):
                if(counter < k):
                    returnArray.append(bucketSort[i][j])
                    counter += 1
                else:
                    break
        return returnArray
