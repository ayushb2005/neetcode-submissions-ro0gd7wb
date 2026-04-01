class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        sliding window
        if next element is smaller then just switch to that one
        if not then move to next element and continue until you find something 
        smaller
        keep an array and return the max
        '''
        arr = []
        prev = 101
        for price in prices:
            if(price < prev):
                prev = price
            else:
                arr.append(price-prev)
            print(prev)
        if(len(arr) == 0):
            return 0
        else:
            return max(arr)
            