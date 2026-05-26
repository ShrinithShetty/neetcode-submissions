class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = [0] * 26
        counts2 = [0] * 26

        if len(s1) > len(s2):
            return False

        for c in range(len(s1)):
            counts1[ord(s1[c])-97] += 1
            counts2[ord(s2[c])-97] += 1

        if counts1 == counts2:
            return True

        l = 0

        for r in range(len(s1),len(s2)):
            counts2[ord(s2[r])-97] += 1
            counts2[ord(s2[l])-97] -= 1
            l += 1

            if counts1 == counts2:
                return True

        return False

        