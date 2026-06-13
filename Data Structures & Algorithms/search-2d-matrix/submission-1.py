class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            left = 0 
            right = len(matrix[i])-1
            while(left <= right):
                middle = (left + right) // 2
                if(matrix[i][middle] == target):
                    return True
                elif(matrix[i][middle] < target):
                    left = middle + 1
                else:
                    right = middle - 1
        return False