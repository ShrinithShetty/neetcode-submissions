class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = deque()
        visited = set()

        def bfs(i,j):
            if i < 0 or i >= m or j < 0  or j >= n or (i,j) in visited or grid[i][j] == -1:
                return 
            else:
                q.append([i,j])
                visited.add((i,j))







        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visited.add((i,j))

        dist = 0

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist

                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)

            dist += 1