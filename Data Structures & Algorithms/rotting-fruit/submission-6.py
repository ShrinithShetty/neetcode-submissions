class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        num_of_fresh = 0
        num_of_min = -1

        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN:
                    q.append([i,j])
                elif grid[i][j] == FRESH:
                    num_of_fresh += 1

        if num_of_fresh == 0:
            return 0

        while q:
            size_q = len(q)
            num_of_min += 1
            for _ in range(size_q):
                i,j = q.popleft()

                for r, c in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == FRESH:
                        grid[r][c] = ROTTEN
                        num_of_fresh -= 1
                        q.append([r,c])

        if num_of_fresh == 0:
            return num_of_min
        else:
            return -1
