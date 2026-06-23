class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        sol = []
        res = []
        n = len(candidates)

        def backtrack(i, curr_sum):
            
            if curr_sum == target:
                res.append(sol[:])
                return 

            if curr_sum > target or i == n:
                return

            sol.append(candidates[i])
            backtrack(i+1,curr_sum+candidates[i])
            sol.pop()

            while i + 1 < n and candidates[i] == candidates[i+1]:
                i += 1

            backtrack(i+1, curr_sum)

        backtrack(0,0)
        return res


            