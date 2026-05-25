class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp = [0] * 26

        for i in s:
            temp[ord(i)-97] += 1
        for i in t:
            temp[ord(i)-97] -= 1

        for count in temp:
            if count!= 0:
                return False
        return True