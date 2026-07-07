class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse = True)
        adj = defaultdict(list)

        for a, b in tickets:
            adj[a].append(b)

        res = []

        def dfs(src):
            while adj[src]:
                next_dest = adj[src].pop()
                dfs(next_dest)
            res.append(src)




        dfs('JFK')
        return res[::-1]
