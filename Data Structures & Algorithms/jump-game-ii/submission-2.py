class Solution:
    def jump(self, nums: List[int]) -> int:

        total = 0 
        res = 0 
        smallest = 0
        far, end = 0, 0

        for i in range(len(nums)-1):
            total += nums[i]
            far = max(far, nums[i] + i)
            if i == end:
                smallest += 1
                end = far

        return smallest
        