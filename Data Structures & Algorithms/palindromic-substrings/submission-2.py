class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPalind(s,i,i)
            res += self.countPalind(s,i,i+1)
        
        return res


    def countPalind(self,s,l,r):
            res = 0
            while 0 <= l and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res