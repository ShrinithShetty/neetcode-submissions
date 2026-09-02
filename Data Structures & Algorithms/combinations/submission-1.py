class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sol = [], []
        def backtrack(i):
            if len(sol) == k:
                res.append(sol[:])
                return 

            left = i
            need = k - len(sol)
            if left > need:
                backtrack(i-1)

            sol.append(i)
            backtrack(i-1)
            sol.pop()

        backtrack(n)
        return res

