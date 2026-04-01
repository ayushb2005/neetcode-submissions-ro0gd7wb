class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        find the multiplication of all of them 
        for each index if not 0 just divide by the 
        keep one with 0 and one without 0 
        if 2 zeros then everything is 0 no matter what
        '''
        zeroCount = 0
        mult = 1
        for i in nums:
            if(i == 0):
                zeroCount += 1
            else:
                mult = mult * i
        if(zeroCount > 1):
            return [0]*len(nums)
        elif(zeroCount == 1):
            outputArray = [0]*len(nums)
            zeroIndex = nums.index(0)
            outputArray[zeroIndex] = mult
            return outputArray
        else:
            outputArray = []
            for i in nums:
                outputArray.append(int(mult/i))
            return outputArray
        return []


