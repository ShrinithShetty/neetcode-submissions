from math import ceil, floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for s in tokens:
            if s in '+-/*':
                b, a = stk.pop(), stk.pop()

                if s == "+":
                    stk.append(a+b)
                elif s == "-":
                    stk.append(a-b)
                elif s == "*":
                    stk.append(a*b)
                else:
                    division = a/b
                    if division < 0:
                        stk.append(ceil(division))
                    else:
                        stk.append(floor(division))

            else:
                stk.append(int(s))

        return stk[0]
        