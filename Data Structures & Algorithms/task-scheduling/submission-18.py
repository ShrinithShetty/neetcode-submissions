class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = []

        for val in count.values():
            heap.append(-val)

        q = deque()
        time = 0
        heapq.heapify(heap)

        while q or heap:
            time += 1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append([cnt, time+n])

            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time