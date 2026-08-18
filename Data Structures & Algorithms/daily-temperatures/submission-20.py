class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        temp = temperatures
        ans = [0] * len(temp)

        for i, t in enumerate(temp):
            while stk and stk[-1][0] < t:
                stk_t, stk_i = stk.pop()
                ans[stk_i] = i - stk_i
            stk.append([t,i])

        return ans