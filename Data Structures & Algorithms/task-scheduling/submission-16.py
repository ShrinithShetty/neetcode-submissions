class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = []

        for val in counter.values():
            heap.append(-val)


        heapq.heapify(heap)
        q = deque()
        time = 0

        while heap or q:
            time += 1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][-1] == time:
                heapq.heappush(heap,q.popleft()[0])

        return time