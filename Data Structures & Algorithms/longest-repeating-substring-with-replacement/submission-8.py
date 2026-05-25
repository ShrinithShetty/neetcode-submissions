class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0

        countS = [0] * 26

        for r in range(len(s)):
            countS[ord(s[r])-65]  += 1

            while (r-l+1)-max(countS) > k:
                countS[ord(s[l])-65] -= 1
                l += 1
            
            longest = max(longest,sum(countS))
        return longest