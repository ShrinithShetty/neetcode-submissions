class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minHeap = [(grid[0][0],0 ,0)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]


        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            if r == N-1 and c == N-1:
                return t
            for dr, dc in directions:
                neir, neic = r+dr, c+dc
                if (0 <= neir < N and 0 <= neic < N and (neir,neic) not in visit):
                    visit.add((neir,neic))
                    heapq.heappush(minHeap, (max(t, grid[neir][neic]), neir, neic))
        