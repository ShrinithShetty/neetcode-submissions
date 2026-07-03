class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)


        UNSEEN, VISITING, VISITED = 0, 1, 2

        states = [UNSEEN] * numCourses

        def dfs(node):
            if states[node] == VISITING: return False
            elif states[node] == VISITED: return True

            states[node] = VISITING

            for nei in g[node]:
                if not dfs(nei):
                    return False
                
            states[node] = VISITED
            return True


        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True