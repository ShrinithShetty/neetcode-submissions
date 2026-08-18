class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)

        tot = m*n

        l, r = 0, tot-1

        while l <= r:
            mid = (l+r)//2
            row = mid//m
            col = mid%m

            val = matrix[row][col]

            if val == target:
                return True
            elif val > target:
                r -= 1
            else:
                l += 1
        return False