class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        long = 0
        n = len(prices)

        for i in range(n):
            for j in range(i+1,n):
                profit = prices[j] - prices[i]
                long = max(profit,long)

        return long