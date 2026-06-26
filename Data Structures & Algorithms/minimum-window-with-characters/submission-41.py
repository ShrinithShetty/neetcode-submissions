class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        freqs = {}
        freqt = {}


        for c in t:
            freqt[c] = 1 + freqt.get(c, 0)

        have, need = 0, len(freqt)
        res, reslen = [-1,-1], float('inf')

        l = 0

        for r in range(len(s)):
            c = s[r]
            freqs[c] = 1 + freqs.get(c,0)

            if c in freqt and freqt[c] == freqs[c]:
                have += 1


            while have == need:
                if reslen > r-l+1:
                    res = [l,r]
                    reslen = r-l+1

                freqs[s[l]] -= 1
                if s[l] in freqt and freqs[s[l]] < freqt[s[l]]:
                    have -= 1
                l += 1

        l, r = res

        return s[l:r+1] if reslen != float('inf') else ""

                


        