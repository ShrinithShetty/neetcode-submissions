class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        counts = {}
        countt = {}


        for c in t:
            countt[c] = 1 + countt.get(c,0)

        need, have = len(countt), 0
        res, reslen = [-1,-1], float('inf')


        l = 0

        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r],0)

            if s[r] in countt and counts[s[r]] == countt[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < reslen:
                    res = [l,r]
                    reslen = r - l + 1

                counts[s[l]] -= 1
                if s[l] in countt and counts[s[l]] < countt[s[l]]:
                    have -= 1

                l += 1

        l, r = res

        return s[l:r+1] if reslen != float('inf') else ""


        