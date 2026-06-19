class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(i, curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return

            if curr_sum > target or i == len(nums):
                return

            sol.append(nums[i])
            backtrack(i, curr_sum + nums[i])
            sol.pop()

            backtrack(i+1,curr_sum)

        backtrack(0,0)
        return res