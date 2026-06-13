class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sf = {}
        tf = {}


        for c in t:
            tf[c] = 1 + tf.get(c,0)

        have, need = 0, len(tf)
        res, reslen = [-1,-1], float('inf')

        l = 0

        for r in range(len(s)):
            c = s[r]
            sf[c] = 1 + sf.get(c,0)

            if c in t and tf[c] == sf[c]:
                have += 1

            while have == need:
                if reslen > (r-l+1):
                    res = [l,r]
                    reslen = r-l+1

                sf[s[l]] -= 1
                if s[l] in t and tf[s[l]] > sf[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if reslen != float('inf') else ""