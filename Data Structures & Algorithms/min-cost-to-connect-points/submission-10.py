class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        seen = set()


        total_cost = 0


        minHeap = [(0,0)]



        while len(seen) < n:
            dist, i = heapq.heappop(minHeap)
            if i in seen:
                continue
            seen.add(i)
            total_cost += dist

            x, y = points[i]
            for j in range(n):
                if j not in seen:
                    xj,yj = points[j]
                    nei = abs(x-xj) + abs(y-yj)
                    heapq.heappush(minHeap, (nei,j))

        return total_cost
        