class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x,y):
            return x**2+y**2

        minHeap = []

        for x, y in points:
            d = dist(x,y)
            if len(minHeap) < k:
                heapq.heappush(minHeap,[-d,x,y])
            else:
                heapq.heappushpop(minHeap, [-d,x,y])

        return [(x,y) for d,x,y in minHeap]


