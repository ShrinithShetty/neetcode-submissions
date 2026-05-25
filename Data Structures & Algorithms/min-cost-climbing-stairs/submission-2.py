class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        step = [0]*n
        step[0] = cost[0]
        step[1] = cost[1]

        for i in range(2,n):
            step[i] = cost[i] + min(step[i-1],step[i-2])

        return min(step[n-1],step[n-2])