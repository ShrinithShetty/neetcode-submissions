class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False

        target = sum(nums)//2
        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            dap = set()
            for t in dp:
                dap.add(t+nums[i])
                dap.add(t)
            dp = dap

        return True if target in dp else False
                