class Solution:
    def trap(self, height: List[int]) -> int:
        lwall = rwall = 0

        lmax = [0] * len(height)
        rmax = [0] * len(height)


        for i in range(len(height)):
            j = -i-1
            lmax[i] = lwall
            rmax[j] = rwall

            lwall = max(lwall,height[i])
            rwall = max(rwall,height[j])

        res = 0

        for i in range(len(height)):
            pot = min(lmax[i],rmax[i])
            res += max(0, pot-height[i])

        return res        