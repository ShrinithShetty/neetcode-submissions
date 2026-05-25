class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        n = len(nums)
        buckets = [0] * (n+1)


        for num, val in counter.items():
            if buckets[val] == 0:
                buckets[val] = [num]
            else:
                buckets[val].append(num)

        lst = []

        for i in range(len(nums),-1,-1):
            if buckets[i] != 0:
                lst.extend(buckets[i])
            if len(lst) == k:
                break

        return lst

