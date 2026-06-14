from math import ceil,floor

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in tokens:
            if i not in '+-*/':
                stk.append(int(i))
            else:
                b, a = stk.pop(), stk.pop()

                if i == '+':
                    stk.append(a+b)
                elif i == '-':
                    stk.append(a-b)
                elif i == '*':
                    stk.append(a*b)
                else:
                    div = a/b
                    if div > 0:
                        stk.append(floor(div))
                    else:
                        stk.append(ceil(div))

        return stk[0]


        