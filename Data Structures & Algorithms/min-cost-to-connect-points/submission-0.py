class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        seen = set()
        minHeap = [(0,0)]
        total_cost = 0

        while len(seen) < n:
            dist, i = heapq.heappop(minHeap)
            if i in seen:
                continue
            seen.add(i)
            x, y = points[i]
            total_cost += dist

            for j in range(n):
                if j not in seen:
                    xj, yj = points[j]
                    nei_dist = abs(x-xj) + abs(y-yj)
                    heapq.heappush(minHeap, (nei_dist, j))


        return total_cost

            


        