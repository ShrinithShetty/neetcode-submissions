class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        n = len(nums)
        buckets = [0] * (n+1)

        for val, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [val]
            else:
                buckets[freq].append(val)

        lst = []

        for i in range(n,-1,-1):
            if buckets[i] != 0:
                lst.extend(buckets[i])
            if len(lst) == k:
                break
        
        return lst



        