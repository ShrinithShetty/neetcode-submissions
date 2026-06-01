class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            m = (l+r)//2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        min_ind = r

        if min_ind == 0:
            l, r = 0, len(nums)-1

        elif nums[0] <= target and target <= nums[min_ind-1]:
            l, r = 0, min_ind
        else:
            l, r = min_ind, len(nums)-1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m-1
            else:
                l = m+1
        return -1