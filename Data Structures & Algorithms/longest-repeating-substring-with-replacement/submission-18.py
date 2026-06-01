class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        freq = [0] * 26
        l = 0
        for r in range(len(s)):
            freq[ord(s[r])-65] += 1
            while (r-l+1) - max(freq) > k:
                freq[ord(s[l])-65] -= 1
                l += 1
            longest = max(longest,r-l+1)

        return longest
