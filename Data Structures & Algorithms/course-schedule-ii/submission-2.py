class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        g = defaultdict(list)

        for a, b in prerequisites:
            g[a].append(b)

        UNSEEN, VISITING, VISITED = 0, 1, 2

        states = [UNSEEN] * numCourses

        def dfs(i):
            if states[i] == VISITED: return True
            elif states[i] == VISITING: return False

            states[i] = VISITING

            for nei in g[i]:
                if not dfs(nei):
                    return False

            states[i] = VISITED
            order.append(i)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []

        return order