from math import floor, ceil
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for s in tokens:
            if s in '+-*/':
                b, a = stk.pop(),stk.pop()

                if s == '+':
                    stk.append(a+b)
                elif s == '-':
                    stk.append(a-b)
                elif s == '*':
                    stk.append(a*b)

                else:
                    div = a/b
                    if div < 0:
                        stk.append(ceil(div))
                    else:
                        stk.append(floor(div))

            else:
                stk.append(int(s))

        return stk[0]
        