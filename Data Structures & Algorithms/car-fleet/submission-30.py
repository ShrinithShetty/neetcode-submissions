class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []

        pairs = [(p,s) for p, s in zip(position, speed)]

        pairs.sort(reverse = True)

        for p, s in pairs:
            stk.append((target-p)/s)
            while len(stk) > 1 and stk[-2] >= stk[-1]:
                stk.pop()

        return len(stk) 