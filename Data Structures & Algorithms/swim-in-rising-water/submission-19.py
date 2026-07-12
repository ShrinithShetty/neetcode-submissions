class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minHeap = [(grid[0][0],0,0)]
        seen = set()
        res = 0
        directions = [(0,1),(1,0),(-1,0),(0,-1)]



        while minHeap:
            time, r, c = heapq.heappop(minHeap)
            if r == N-1 and c == N-1:
                return time
            for dr , dc in directions:
                neir, neic = r+dr, c+dc
                if 0 <= neir < N and 0 <= neic < N and (neir, neic) not in seen:
                    heapq.heappush(minHeap, ((max(grid[neir][neic],time)),neir, neic))
                    seen.add((neir, neic))

        

            