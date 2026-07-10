class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        minHeap = [(0,0)]
        total_dist = 0

        seen = set()


        while len(seen) < n:
            dist, i = heapq.heappop(minHeap)
            if i in seen:
                continue
            seen.add(i)
            total_dist += dist
            x, y = points[i]
            for j in range(n):
                if j not in seen:
                    xj, yj = points[j]
                    neidist = abs(x-xj) + abs(y-yj)
                    heapq.heappush(minHeap, (neidist, j))


        return total_dist