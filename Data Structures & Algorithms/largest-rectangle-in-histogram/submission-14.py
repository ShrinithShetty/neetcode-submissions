class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        n = len(heights)
        max_ar = 0



        for i , height in enumerate(heights):
            start = i
            while stk and stk[-1][0] > height:
                h, j = stk.pop()
                w = i - j
                max_ar = max(max_ar, h*w)
                start = j
            stk.append((height,start))

        while stk:
            h, j = stk.pop()
            w = n - j
            max_ar = max(max_ar, h*w)

        return max_ar
                



        