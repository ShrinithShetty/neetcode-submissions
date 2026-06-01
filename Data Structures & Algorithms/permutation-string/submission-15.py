class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        f1 = [0] * 26
        f2 = [0] * 26

        for r in range(len(s1)):
            f1[ord(s1[r])-97] += 1
            f2[ord(s2[r])-97] += 1

        if f1 == f2:
            return True

        l = 0
        for r in range(len(s1),len(s2)):
            f2[ord(s2[r])-97] += 1
            f2[ord(s2[l])-97] -= 1
            l += 1      

            if f1 == f2:
                return True
        return False