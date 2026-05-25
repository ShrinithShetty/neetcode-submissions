class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        n = len(heights)
        max_area = 0


        for i, h in enumerate(heights):
            start = i
            while stk and h < stk[-1][0]:
                ph, j = stk.pop()
                w = i - j
                a = ph * w
                max_area = max(max_area,a)
                start = j

            stk.append((h,start))

        while stk:
                ph, j = stk.pop()
                w = n - j
                a = ph * w
                max_area = max(max_area,a)
        return max_area