class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        if nums == []:
            return 0

        for num in nums:
            seq = 1
            
            while num + 1 in nums:
                seq += 1
                num = num + 1
                count = max(count, seq)
        return count