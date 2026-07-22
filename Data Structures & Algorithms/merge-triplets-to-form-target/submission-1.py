class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        '''
        
        '''
        found1 = False
        found2 = False
        found3 = False
        for i in triplets:
            if i[0] > target[0] or \
            i[1] > target[1] or i[2] > target[2]:
                continue
            if i[0] == target[0]:
                found1 = True
            if i[1] == target[1]:
                found2 = True
            if i[2] == target[2]:
                found3 = True
        return found1 and found2 and found3
             