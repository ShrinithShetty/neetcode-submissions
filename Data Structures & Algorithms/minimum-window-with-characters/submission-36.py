class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        sf = {}
        tf = {}

        for c in t:
            tf[c] = 1 + tf.get(c,0)
        
        l = 0
        res, reslen = [-1,-1], float('inf')
        have, need = 0, len(tf)

        for r in range(len(s)):
            c = s[r]
            sf[c] = 1 + sf.get(c,0)
            if c in t and sf[c] == tf[c]:
                have += 1

            while have == need:
                if reslen > r-l+1:
                    res = [l,r]
                    reslen = r-l+1
                sf[s[l]] -= 1
                if s[l] in t and sf[s[l]] < tf[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if reslen != float('inf') else ""


      