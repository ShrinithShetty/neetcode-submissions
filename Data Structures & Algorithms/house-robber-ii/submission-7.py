class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, nums):
            n = len(nums)
            if n==1:
                return nums[0]
            if n == 2:
                return max(nums[0], nums[1])

            prev, curr = nums[0], max(nums[0],nums[1])

            for i in range(2, n):
                prev, curr = curr, max(curr, nums[i] + prev)

            return curr