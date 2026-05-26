class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt ={}


        for st in strs:
            count = [0]*26
            for s in st:
                count[ord(s)-97] += 1

            count = tuple(count)
            if count in dictt:
                dictt[count].append(st)
            else:
                dictt[count] = [st]

        return list(dictt.values())
