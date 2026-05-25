class MinStack:

    def __init__(self):
        self.stk = []
        self.Minstk = []
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        val = min(val,self.Minstk[-1] if self.Minstk else val)
        self.Minstk.append(val)
        

    def pop(self) -> None:
        self.stk.pop()
        self.Minstk.pop()
        

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.Minstk[-1]
        
