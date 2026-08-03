class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n-1

        for i in range(len(nums)-1,-1,-1):
            jump = nums[i]

            if jump + i >= target:
                target = i

        return target == 0