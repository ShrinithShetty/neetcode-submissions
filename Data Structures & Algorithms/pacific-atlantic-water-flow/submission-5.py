class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        p_que = deque()
        p_seen = set()

        a_que = deque()
        a_seen = set()


        for j in range(n):
            p_que.append((0,j))
            p_seen.add((0,j))

        for i in range(1,m):
            p_que.append((i,0))
            p_seen.add((i,0))

        for i in range(m):
            a_que.append((i, n-1))
            a_seen.add((i,n-1))

        for j in range(n-1):
            a_que.append((m-1,j))
            a_seen.add((m-1,j))


        def coord(que, seen):
            while que:
                i,j = que.popleft()
                for i_off, j_off in [(1,0),(-1,0),(0,1),(0,-1)]:
                    r, c = i+i_off, j+j_off
                    if 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[i][j] and (r,c) not in seen:
                        que.append((r,c))
                        seen.add((r,c))

        coord(p_que,p_seen)
        coord(a_que,a_seen)

        return list(p_seen.intersection(a_seen))
