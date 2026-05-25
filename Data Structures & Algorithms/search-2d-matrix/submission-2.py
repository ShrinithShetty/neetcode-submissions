class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
         m = len(matrix)
         n = len(matrix[0])
         t = n * m
         l = 0
         r = t - 1

         while l <= r:
            mid = (l+r) // 2
            row = mid//n
            col = mid%n

            mid_num = matrix[row][col]
            if target == mid_num:
                return True
            elif target < mid_num:
                r = mid - 1
            else:
                l = mid+1
         return False




        