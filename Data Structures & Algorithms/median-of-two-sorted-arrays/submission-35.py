class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        a = nums1
        b = nums2

        full = len(a) + len(b)
        half = full//2

        if len(a) > len(b):
            a, b = b, a

        

        l, r = 0, len(a)-1

        while True:
            i = (l+r)//2
            j = half - i - 2

            aleft = a[i] if i >= 0 else float('-inf')
            aright = a[i + 1] if i + 1 < len(a) else float('inf') 
            bleft = b[j] if j >= 0 else float('-inf')
            bright = b[j+1] if j+1 < len(b) else float('inf')


            if aleft <= bright and bleft <= aright:
                if full%2:
                    return min(aright,bright)
                return (max(aleft,bleft)+min(aright,bright))/2

            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1