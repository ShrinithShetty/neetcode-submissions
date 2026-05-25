class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def roblinear(array):
            prev1 = 0
            prev2 = 0
            for money in array:
                curr = max(prev1,prev2+money)
                prev2 = prev1
                prev1 = curr
            return prev1 
        return max(roblinear(nums[1:]),roblinear(nums[:-1])) 
        