class Solution:
    def isValid(self, s: str) -> bool:
        dictt = {']':'[','}':'{',')':'('}
        stk = []
        for i in s:
            if i not in dictt:
                stk.append(i)
            else:
                if not stk:
                    return False
                else:
                    p = stk.pop()
                    if p != dictt[i]:
                        return False

        return not stk    