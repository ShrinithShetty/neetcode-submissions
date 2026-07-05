class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        def capture(i,j):
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'T'
                capture(i+1,j)
                capture(i-1,j)
                capture(i,j-1)
                capture(i,j+1)


        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i in [0, m-1] or j in [0,n-1]):
                    capture(i,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = "O"