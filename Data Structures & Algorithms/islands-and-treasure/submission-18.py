class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        visited = set()
        dist = 0

        def bfs(i,j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] != -1 and (i,j) not in visited:
                q.append([i,j])
                visited.add((i,j))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visited.add((i,j))


        while q:
            size_q = len(q)

            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)

            
            dist += 1





        