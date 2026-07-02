class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        num_of_min = -1
        num_of_fresh = 0
        EMPTY, FRESH, ROTTEN = 0,1,2


        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN:
                    q.append([i,j])
                elif grid[i][j] == FRESH:
                    num_of_fresh += 1


        if num_of_fresh == 0:
            return 0

        while q:
            num_of_min += 1
            q_size = len(q)
            for _ in range(q_size):
                r,c = q.popleft()
                for r, c in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == FRESH:
                        grid[r][c] = ROTTEN
                        q.append([r,c])
                        num_of_fresh -= 1

        if num_of_fresh == 0:
            return num_of_min
        else:
            return -1



            

