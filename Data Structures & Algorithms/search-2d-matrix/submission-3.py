class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t = m*n
        l,r = 0 , t-1

        while l <= r:
            mid = (l+r)//2
            row = mid//n
            col = mid%n

            val = matrix[row][col]
            if val == target:
                return True
            elif val > target:
                r = mid - 1
            else:
                l = mid+1

        return False
