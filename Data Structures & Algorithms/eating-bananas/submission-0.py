class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        try from 1 to max of array
        '''
        left = 1
        right = max(piles)
        k = right
        while(left <= right):
            middle = (left + right) // 2
            current = 0
            for i in piles:
                current += math.ceil(i/middle)
            if(current <= h):
                k = min(middle, k)
                right = middle - 1
            else:
                left = middle + 1
        return k
