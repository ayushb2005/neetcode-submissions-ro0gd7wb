class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        counter = len(nums)
        while( counter > k):
            heapq.heappop(nums)
            counter -= 1
        return nums[0]