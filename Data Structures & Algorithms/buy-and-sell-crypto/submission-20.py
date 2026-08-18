class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        min_price = float('inf')

        for price in prices:
            if min_price > price:
                min_price = price
            profit = price - min_price

            max_prof = max(max_prof, profit)

        return max_prof