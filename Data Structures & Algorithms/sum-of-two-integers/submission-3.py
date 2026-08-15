class Solution:
    def getSum(self, a: int, b: int) -> int:
        Mask = 0xFFFFFFFF
        Max_Int = 0x7FFFFFFF


        while b != 0:
            a, b = (a ^ b) & Mask, ((a & b)<<1) & Mask

        return a if a <= Max_Int else ~(a ^ Mask)