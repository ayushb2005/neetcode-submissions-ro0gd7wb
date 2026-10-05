class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1

        while left <= right:
            middle = (left + right) // 2
            if matrix[middle][0] <= target <= matrix[middle][len(matrix[middle])-1] :
                leftInside = 0
                rightInside = len(matrix[middle]) - 1
                while leftInside <= rightInside:
                    middleInside = (leftInside + rightInside) // 2
                    if matrix[middle][middleInside] == target:
                        return True
                    elif matrix[middle][middleInside] > target:
                        rightInside -= 1
                    else:
                        leftInside += 1
                return False
            elif matrix[middle][0] > target:
                right -= 1
            elif matrix[middle][len(matrix[middle])-1] < target:
                left += 1
        return False
