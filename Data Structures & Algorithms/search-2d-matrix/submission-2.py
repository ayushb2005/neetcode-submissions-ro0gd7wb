class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in range(len(matrix)):
        #     left = 0 
        #     right = len(matrix[i])-1
        #     while(left <= right):
        #         middle = (left + right) // 2
        #         if(matrix[i][middle] == target):
        #             return True
        #         elif(matrix[i][middle] < target):
        #             left = middle + 1
        #         else:
        #             right = middle - 1
        # return False
        left = 0
        right = len(matrix)-1
        while(left <= right):
            middle = (left + right) // 2
            if(matrix[middle][0] <= target <= matrix[middle][-1]):
                lRow = 0
                rRow = len(matrix[middle])-1
                while(lRow <= rRow):
                    mRow = (lRow + rRow) // 2
                    if(target == matrix[middle][mRow]):
                        return True
                    elif(matrix[middle][mRow] > target):
                        rRow = mRow - 1
                    else:
                        lRow = mRow + 1
                return False
            elif(target < matrix[middle][0]):
                right = middle - 1
            else:
                left = middle + 1
        return False
