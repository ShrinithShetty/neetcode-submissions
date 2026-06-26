class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False


        freq1 = [0]*26
        freq2 = [0]*26


        for i in range(len(s1)):
            freq1[ord(s1[i])-97] += 1
            freq2[ord(s2[i])-97] += 1

        if freq1 == freq2:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            freq2[ord(s2[r])-97] += 1
            freq2[ord(s2[l])-97] -= 1
            l += 1

            if freq1 == freq2:
                return True

        return False 
        