class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        p_q = deque()
        p_seen = set()

        a_q = deque()
        a_seen = set()

        for j in range(n):
            p_q.append((0,j))
            p_seen.add((0,j))

        for i in range(1,m):
            p_q.append((i,0))
            p_seen.add((i,0))

        for i in range(m):
            a_q.append((i,n-1))
            a_seen.add((i,n-1))

        for j in range(n-1):
            a_q.append((m-1,j))
            a_seen.add((m-1,j))


        def coord(q,s):
            while q:
                i, j = q.popleft()
                for i_off, j_off in [(1,0),(0,1),(-1,0),(0,-1)]:
                    r,c = i+i_off, j+j_off
                    if 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[i][j] and (r,c) not in s:
                        q.append((r,c))
                        s.add((r,c))

        coord(p_q,p_seen)
        coord(a_q, a_seen)

        return list(p_seen.intersection(a_seen))
