class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        CurrMax, CurrMin = 1, 1

        for n in nums:

            temp = CurrMax * n
            CurrMax = max(CurrMax * n, CurrMin * n, n)
            CurrMin = min(temp, CurrMin * n, n)

            res = max(res, CurrMax)

        return res 