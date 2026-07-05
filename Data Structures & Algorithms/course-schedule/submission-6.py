class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for a, b in prerequisites:
            adj[a].append(b)

        UNSEEN, VISITING, VISITED = 0, 1, 2

        states = [UNSEEN] * numCourses

        def dfs(node):
            if states[node] == VISITED: return True
            elif states[node] == VISITING: return False

            states[node] = VISITING

            for nei in adj[node]:
                if not dfs(nei):
                    return False
            states[node] = VISITED
            return True



        for i in range(numCourses):
            if not dfs(i):
                return False

        return True