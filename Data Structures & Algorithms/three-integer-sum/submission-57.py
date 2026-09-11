class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []


        for a in range(len(nums)):
            if nums[a] > 0:
                break
            if a > 0 and nums[a] == nums[a-1]:
                continue

            pairs = self.isequal(nums, a + 1, -nums[a])
            for pair in pairs:
                res.append([nums[a]] + pair)
        return res


    def isequal(self, nums, b, target):
        pairs = []
        l, r = b, len(nums) - 1
        while l < r:
            if target == nums[l] + nums[r]:
                pairs.append([nums[l], nums[r]])
                l += 1
                r -= 1

                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
            elif target > nums[l] + nums[r]:
                l += 1
            else:
                r -= 1
        return pairs

        