class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        bucket sort correlating to the amount of times an element shows 
        up, then go backwards and pick the k most elements
        '''
        #create amount of buckets for the length of arr
        countElementFrequency = {}
        for i in nums:
            if i in countElementFrequency:
                countElementFrequency[i] += 1
            else:
                countElementFrequency[i] = 1
        bucketList = []
        print(countElementFrequency)
        for i in nums:
            bucketList.append([])
        for i in countElementFrequency.keys():
            bucketList[countElementFrequency[i]-1].append(i)
        outputArr = [] 
        print(bucketList)
        for i in range(len(bucketList)-1, -1, -1):
            print(bucketList[i])
            for j in range(len(bucketList[i])-1, -1, -1):
                outputArr.append(bucketList[i][j])
                if(len(outputArr)==k):
                    return outputArr
        return []
