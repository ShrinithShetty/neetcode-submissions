import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            secondlargest = heapq.heappop(stones)

            if largest != secondlargest:
                heapq.heappush(stones, largest-secondlargest)

        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0
