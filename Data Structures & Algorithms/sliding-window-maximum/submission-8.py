class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        have a deque which is decreasing
        keep adding numbers that are < than the top of the deq
        otherwise if larger then keep popping from the deq until its in
        the correct place
        the largest number will always be the left side of the deq
        '''
        deq = deque()
        maxArray = []

        for i in range(len(nums)):
            while(deq and nums[deq[-1]] < nums[i]):
                deq.pop()
            deq.append(i)
            if(deq and deq[0] <= i-k):
                deq.popleft()
            if(i >= k-1 and deq):
                #record max
                maxArray.append(nums[deq[0]])
        return maxArray



                

