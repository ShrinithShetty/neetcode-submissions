class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]


        heapq.heapify(stones)

        while len(stones) > 1:
            large = heapq.heappop(stones)
            seclarge = heapq.heappop(stones)

            if large != seclarge:
                heapq.heappush(stones, large-seclarge)


        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0

        