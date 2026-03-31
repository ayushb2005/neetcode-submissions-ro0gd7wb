class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create bucket of elements
        #add them to a 2d array where each array index represents the elements with x amounts of nums in arr

        numsMap = {}

        for i in nums:
            numsMap[i] = numsMap.get(i,0)+1
        #create a bucket [[1],[2],[3]]
        counter = 0
        # bucket = [[]]*len(nums)
        bucket = []
        for _ in range(len(nums)):
            bucket.append([])
        for i in numsMap:
            bucket[numsMap[i]-1].append(i)
        print(bucket)
        kFreqNumsList = [] 
        #loop backwards through the buckets 
        #option 2 i can combine all buckets then go backwards by k elements
        for i in range(len(bucket)-1,-1,-1):
            for j in bucket[i]:
                kFreqNumsList.append(j)
                if(len(kFreqNumsList) == k):
                    return kFreqNumsList
        return []


            
        return []