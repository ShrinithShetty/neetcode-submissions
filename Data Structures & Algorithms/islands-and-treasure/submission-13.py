class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = deque()
        visited = set()

        def bfs(r,c):
            if 0 <= r < m and 0 <= c < n and grid[r][c] != -1 and (r,c) not in visited:
                q.append([r,c])
                visited.add((r,c))
            
            


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visited.add((i,j))

        dist = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c-1)
                bfs(r,c+1)

            dist += 1

        