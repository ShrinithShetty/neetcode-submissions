class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stk = []

        for i, t in enumerate(temperatures):
            while stk and stk[-1][0] < t:
                stk_t, stk_i = stk.pop()
                answer[stk_i] = i - stk_i
            stk.append([t,i])
        return answer        