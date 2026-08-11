class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0

        prevE = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevE:
                prevE = end
            else:
                res += 1
                prevE = min(end, prevE)

        return res
