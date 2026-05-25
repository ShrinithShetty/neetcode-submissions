class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts = {}

        for i, n in enumerate(nums):
            if target - n in dicts:
                return [dicts[target-n],i]
            dicts[n] = i