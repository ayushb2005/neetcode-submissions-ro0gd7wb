class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        need a sorted array
        stay on one index
        then two pointer staregy to get the other two values that sum to 0
        take the sum of the two pointers 
        if sum is found to 0, ensure no duplicates 
        if sum is positive then move right pointer
        if sum is negative then move left pointer
        then to avoid duplicates once we have found soemthing move
        the left pointer until its a new value and same with right
        -4,-1,-1,0,1,2
        '''
        ouputArray = []
        nums.sort()
        prev = None
        for i in range(len(nums)):
            if(nums[i] >0):
                return ouputArray
            if(prev == nums[i]):
                continue
            else:
                prev = nums[i]
            left = i+1
            right = len(nums)-1
            while(left < right):
                sumOfDigits = nums[i] + nums[left] + nums[right]
                if(sumOfDigits == 0):
                    ouputArray.append([nums[i], nums[left], nums[right]])
                    prevl = nums[left]
                    while(left < right and prevl == nums[left]):
                        left+= 1
                    prevr = nums[right]
                    while(right>left and prevr == nums[right]):
                        right -= 1
                else:
                    if(sumOfDigits > 0):
                        right -=1
                    else:
                        left +=1
                    
        return ouputArray

