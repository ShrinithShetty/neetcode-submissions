class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        t = set()
        longest = 0


        for r in range(len(s)):
            while s[r] in t:
                t.remove(s[l])
                l += 1

            t.add(s[r])
            lenn = r - l + 1
            longest = max(longest,lenn)

        return longest

        