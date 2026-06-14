class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        maxx = 0
        n = len(heights)

        for i, h in enumerate(heights):
            need = i
            while stk and stk[-1][0] > h:
                hi, j = stk.pop()
                w = i - j
                maxx = max(maxx,hi*w)

                need = j
            stk.append((h, need))

        while stk:
            hi, j = stk.pop()

            w = n - j
            maxx = max(maxx,hi*w)

        return maxx


