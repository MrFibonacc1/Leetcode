class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        start, end = 0, len(matrix)-1
        while end >= start:
            midpoint = (start+end)//2
            if target > matrix[midpoint][-1]:
                start = midpoint + 1
            elif target < matrix[midpoint][0]:
                end = midpoint - 1
            else:
                break
        if not(end >=start):
            return False
        matrixVal = (start+end)//2
        start,end = 0, len(matrix[0])
        while end >= start:
            midpoint = (start+end)//2
            value = matrix[matrixVal][midpoint]
            if target > value:
                start = midpoint + 1
            elif target < value:
                end = midpoint - 1
            else:
                return True
        return False
Solution = Solution()
print(Solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],31))