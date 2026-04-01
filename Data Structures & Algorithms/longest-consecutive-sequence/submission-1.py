class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        have a set of the elements
        check for every number if there is num-1 if not then check if num+1 exists
        if it does then keep checking for num+1 until we can't find it 
        if num-1 exists just skip it
        '''

        numsSet = set(nums)
        maxConsecutive = 0
        for num in numsSet:
            if(num-1 not in numsSet):
                maxConsecNum = 1
                value = num+1
                while( value in numsSet):
                    value += 1
                    maxConsecNum += 1
                maxConsecutive = max(maxConsecutive,maxConsecNum )
        return maxConsecutive
            
                