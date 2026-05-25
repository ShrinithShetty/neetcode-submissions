class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dish = defaultdict(list)

        for s in strs:
            temp = [0] * 26
            for i in s:
                temp[ord(i)-97] += 1
            temp = tuple(temp)
            dish[temp].append(s)

        return list(dish.values())