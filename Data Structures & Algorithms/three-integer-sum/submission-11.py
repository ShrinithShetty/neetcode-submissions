class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = [] 
        n = len(nums)
        
        for i in range(n):
            if nums[i] > 0 :
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, n-1 
            while l < r:
                tsum = nums[i] + nums[l] + nums[r]
                

                if tsum == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l, r = l+1,r-1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif tsum < 0:
                    l += 1
                   
                else:
                    r -= 1

        return res
