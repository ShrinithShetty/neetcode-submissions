from math import ceil,floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for c in tokens:
            if c in '+-*/':
                b, a = stk.pop(), stk.pop()

                if c == '+':
                    stk.append(a+b)
                elif c == '*':
                    stk.append(a*b)
                elif c == '-':
                    stk.append(a-b)
                else:
                    division = a/b
                    if division < 0:
                        stk.append(ceil(division))
                    else:
                        stk.append(floor(division))
            else:
                stk.append(int(c)) 
        return stk[0]


        