class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = {}

        for st in strs:
            temp = [0] * 27

            for s in st:
                temp[ord(s)-97] += 1

            temp = tuple(temp)

            if temp in dictt:
                dictt[temp].append(st)
            else:
                dictt[temp] = [st]

        return list(dictt.values())