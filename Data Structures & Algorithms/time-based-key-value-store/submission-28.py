class TimeMap:

    def __init__(self):
        self.dictt = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictt:
            self.dictt[key] = []
        self.dictt[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        val = self.dictt.get(key,[])
        ans = ""

        l, r = 0, len(val)-1
        while l <= r:
            m = (l+r)//2
            if val[m][1] <= timestamp:
                ans = val[m][0]
                l = m + 1
            else:
                r = m - 1
        return ans

        
