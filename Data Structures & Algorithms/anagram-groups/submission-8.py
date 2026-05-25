class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicte = {}

        for st in strs:
            temp = [0] * 30

            for s in st:
                temp[ord(s)-97] += 1


            temp = tuple(temp)
            if temp in dicte:
                dicte[temp].append(st)
            else:
                dicte[temp] = [st]

        return list(dicte.values())
