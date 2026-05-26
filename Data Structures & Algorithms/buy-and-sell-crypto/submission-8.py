class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        minn = float('inf')

        for price in prices:
            if price < minn:
                minn = price
            
            profit = price - minn

            maxx = max(maxx,profit)

        return maxx