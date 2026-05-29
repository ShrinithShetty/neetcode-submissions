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
            l , r = 0, len(nums) - 1

        elif target >= nums[0] and target <= nums[min_ind - 1]:
            l, r = 0, min_ind
        else:
            l, r = min_ind, len(nums) - 1

        
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

                