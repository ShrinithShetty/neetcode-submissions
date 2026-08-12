class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        ans = []
        i, j = 0, 0

        UP, DOWN, RIGHT, LEFT = 0,1,2,3
        direction =  RIGHT

        UP_WALL = 0
        RIGHT_WALL = n
        LEFT_WALL = -1
        DOWN_WALL = m

        while len(ans) != m*n:
            if direction == RIGHT:
                while j < RIGHT_WALL:
                    ans.append(matrix[i][j])
                    j += 1
                direction = DOWN
                RIGHT_WALL -= 1
                i, j = i+1, j-1
            elif direction == DOWN:
                while i < DOWN_WALL:
                    ans.append(matrix[i][j])
                    i += 1
                direction = LEFT
                i, j = i-1, j-1
                DOWN_WALL -= 1
            elif direction == LEFT:
                while j > LEFT_WALL:
                    ans.append(matrix[i][j])
                    j -= 1
                direction =  UP
                i, j = i-1, j+1
                LEFT_WALL += 1

            else:
                while i > UP_WALL:
                    ans.append(matrix[i][j])
                    i -= 1
                direction = RIGHT
                i, j = i+1, j + 1
                UP_WALL += 1

        return ans


            