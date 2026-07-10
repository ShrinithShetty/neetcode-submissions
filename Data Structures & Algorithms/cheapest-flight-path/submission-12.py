class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        points = [float("inf")] * n
        points[src] = 0

        for i in range(k+1):
            tempprices = points.copy()
            for s,d,p in flights:
                if points[s] == float('inf'):
                    continue
                if points[s] + p < tempprices[d]:
                    tempprices[d] = points[s] + p

            points = tempprices

        return -1 if points[dst] == float('inf') else points[dst]