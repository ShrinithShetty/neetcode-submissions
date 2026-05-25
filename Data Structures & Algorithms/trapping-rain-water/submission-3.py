class Solution:
    def trap(self, height: List[int]) -> int:
        lwall = rwall = 0
        n = len(height)

        lmax = [0] * n 
        rmax = [0] * n

        for i in range(n):
            j = -i-1

            lmax[i] = lwall
            rmax[j] = rwall

            lwall = max(lwall,height[i])
            rwall = max(rwall,height[j])

        summ = 0

        for i in range(n):
            pot = min(lmax[i],rmax[i])
            summ += max(0,pot - height[i])

        return summ 
