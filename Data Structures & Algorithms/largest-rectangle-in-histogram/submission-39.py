class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        n = len(heights)
        maxx = 0


        for i, t in enumerate(heights):
            start = i
            while stk and stk[-1][0] > t:
                h, j = stk.pop()
                w = i - j
                a = w * h
                maxx = max(maxx,a)

                start = j
            stk.append((t, start))

        while stk:
            h, j = stk.pop()
            w = n - j

            maxx = max(maxx,h*w)

        return maxx