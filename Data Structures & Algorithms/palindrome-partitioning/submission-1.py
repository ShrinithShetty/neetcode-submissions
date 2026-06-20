class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sol = [], []

        def backtrack(i):
            if i >= len(s):
                res.append(sol[:])
                return

            for j in range(i, len(s)):
                if self.is_pali(s, i, j):
                    sol.append(s[i:j+1])
                    backtrack(j+1)
                    sol.pop()

        backtrack(0)
        return res

    def is_pali(self,s,l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1

        return True 