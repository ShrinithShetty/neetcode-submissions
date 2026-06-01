class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            s = set()
            for i in row:
                if i in s:
                    return False
                elif i != '.':
                    s.add(i)

        for col in range(len(board[0])):
            s = set()
            for row in range(len(board[col])):
                i = board[row][col]
                if i in s:
                    return False
                elif i != '.':
                    s.add(i)

        for current in range(len(board)):
            row_index = 3*(current%3)
            col_index = 3*(current//3)
            s = set()

            for row in range(row_index, row_index+3):
                for col in range(col_index, col_index+3):
                    i = board[row][col]
                    if i in s:
                        return False
                    elif i != '.':
                        s.add(i)

        return True


        