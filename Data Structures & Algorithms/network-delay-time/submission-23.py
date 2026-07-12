class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for a,b, t in times:
            graph[a].append((b,t))


        minHeap = [(0,k)]
        min_time = {}


        while minHeap:
            time_k_t_i, i = heapq.heappop(minHeap)
            if i in min_time:
                continue

            min_time[i] = time_k_t_i

            for nei, neitime in graph[i]:
                if nei not in min_time:
                    heapq.heappush(minHeap, ((time_k_t_i + neitime),nei))

        if len(min_time) == n:
                return max(min_time.values())
        else:
                return -1
