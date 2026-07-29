class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1

        for i in range(len(coins)-1,-1,-1):
            dap = [0] * (amount +1)
            dap[0] = 1

            for a in range(amount+1):
                dap[a] = dp[a]
                if a - coins[i] >= 0:
                    dap[a] += dap[a-coins[i]]

            dp = dap


        return dp[amount]
