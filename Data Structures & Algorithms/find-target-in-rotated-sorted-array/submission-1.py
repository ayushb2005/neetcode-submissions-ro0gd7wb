class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        
        while(l<r):
            mid = int((l+r)/2)
            if(nums[mid] < nums[r]):
                r = mid
            else:
                l = mid + 1
        pivot = l
        if(nums[l] <= target and target <= nums[-1]):
            return self.binarySearch(nums, pivot,len(nums)-1,target)
        else:
            return self.binarySearch(nums, 0, pivot-1,target)
    def binarySearch(self, nums, l, r, target):
        while(l<=r):
            mid = int((l+r)/2)
            if(nums[mid] == target):
                return mid
            elif(nums[mid]<target):
                l = mid + 1
            else:
                r = mid-1
        return -1