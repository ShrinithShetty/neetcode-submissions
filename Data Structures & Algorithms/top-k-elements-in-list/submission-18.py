class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        bucket = [0] * (n+1)


        for val, freq in count.items():
          if bucket[freq] == 0:
            bucket[freq] = [val]
          else:
            bucket[freq].append(val)

        lst = []

        for i in range(n,-1,-1):
          if bucket[i] != 0:
            lst.extend(bucket[i])
          if len(lst) == k:
            break
        return lst

          
 