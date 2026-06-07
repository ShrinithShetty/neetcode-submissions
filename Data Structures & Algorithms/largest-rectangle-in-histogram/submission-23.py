class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        n = len(heights)
        maxx = 0

        for i, t in enumerate(heights):
            sub = i
            while stk and stk[-1][0] > t:
                h, j = stk.pop()
                w = i - j
                maxx = max(maxx,w*h)
                sub = j
            stk.append([t,sub])


        while stk:
            h, i = stk.pop()
            w = n - i
            maxx = max(maxx,w*h)


        return maxx
