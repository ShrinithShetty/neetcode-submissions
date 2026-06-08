from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = 0
        def kworks(n):
            hours = 0
            for pile in piles:
                hours += ceil(pile/n)
            return hours <= h
        l, r = 1, max(piles)
        while l < r:
            m = (l+r)//2
            if kworks(m):
                r = m
            else:
                l = m+1
        return r