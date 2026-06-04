class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if(nums[i] > 0):
                break
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            left = i+1 
            right = len(nums) - 1
            while(left < right):
                triplet = nums[i] + nums[left] + nums[right]
                if(triplet == 0):
                    triplets.append([nums[i], nums[left], nums[right]])
                    leftPrev = nums[left]
                    while(left < right and leftPrev == nums[left]):
                        left += 1
                    rightPrev = nums[right]
                    while(right > left and  rightPrev == nums[right]):
                        right -= 1
                elif(triplet > 0):
                    right -= 1
                elif(triplet < 0):
                    left += 1
        return triplets
            