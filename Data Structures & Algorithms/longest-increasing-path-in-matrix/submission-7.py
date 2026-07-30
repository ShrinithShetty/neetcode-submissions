class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        ROWS, COLS = len(matrix), len(matrix[0])

        def dfs(r,c,prev):
            if 0 > r or r >= ROWS or 0 > c or c >= COLS or prev >= matrix[r][c]:
                return 0

            if (r,c) in dp:
                return dp[(r,c)]
            
            res = 1
            res = max(res, 1 + dfs(r+1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r-1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c+1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c-1, matrix[r][c]))
            dp[(r,c)] = res
            return res



        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j,-1)

        return max(dp.values())
