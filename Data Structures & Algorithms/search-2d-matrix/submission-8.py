class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        t = m*n
        l, r = 0, t-1
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



        


        