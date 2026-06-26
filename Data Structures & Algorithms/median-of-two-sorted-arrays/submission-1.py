class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        get the size of both arrays along with the half value of them 

        with the smaller array do binary search to get the left partition 
        then with the size of the left partiton get the left partition of the larger array
        using half value - left partition of smaller array

        check that the left partitions of both arrays are smaller than each others next index
        1 2 3 4
        2 3 4
        check 3 <= 4 and 3<=4
        for odd array, take the min in the leftmost of the right partitions 
        for even array, take the max of the right of the leftmost and min of the leftmost of the right partitions 
        '''

        size = len(nums1) + len(nums2)
        half = size//2
        if(len(nums2) > len(nums1)):
            nums2, nums1 = nums1, nums2
        left = -1 
        right = len(nums2) - 1
        while(left <= right):
            middle = (left + right) // 2
            leftPartiton = (half-(middle + 1)) - 1
            
            if(middle < 0):
                aLeft = float("-inf")
            else:
                aLeft = nums2[middle]
            if(middle+1 == len(nums2)):
                aRight = float("inf")
            else:
                aRight = nums2[middle + 1]

            if(leftPartiton < 0):
                bLeft = float("-inf")
            else:
                bLeft = nums1[leftPartiton]
            if(leftPartiton+1 == len(nums1)):
                bRight = float("inf")
            else:
                bRight = nums1[leftPartiton + 1]

            if(size % 2 == 0):
                if(aLeft <= bRight and bLeft <= aRight):
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
                else:
                    if(aLeft > bRight):
                        right = middle - 1
                    else:
                        left = middle + 1
            else:
                if(aLeft <= bRight and bLeft <= aRight):
                    return min(aRight, bRight)
                else:
                    if(aLeft > bRight):
                        right = middle - 1
                    else:
                        left = middle + 1
            



