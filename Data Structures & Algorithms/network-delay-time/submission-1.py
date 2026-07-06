class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for a,b, time in times:
            graph[a].append((b,time))

        min_heap = [(0,k)]
        min_time = {}

        while min_heap:
            time_k_to_i, i  = heapq.heappop(min_heap)
            if i in min_time:
                continue
            min_time[i] = time_k_to_i
            for nei, nei_time in graph[i]:
                if nei not in min_time:
                    heapq.heappush(min_heap, (time_k_to_i + nei_time, nei))


        if len(min_time) == n:
            return max(min_time.values())
        else:
            return -1