class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_val = 0
        l = 0
        r = n-1


        while l < r:
            w = r - l
            h = min(heights[l],heights[r])
            a = w * h

            max_val = max(max_val,a)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_val