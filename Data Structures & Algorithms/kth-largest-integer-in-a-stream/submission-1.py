class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.arr = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.arr, val)
        counter = len(self.arr)
        while(counter != self.k):
            heapq.heappop(self.arr)
            counter -= 1
        return self.arr[0]

